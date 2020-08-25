terraform {
  backend "gcs" {
    bucket = "terraform.woltchallenge.app"
    prefix = "terraform/state"
  }

  required_version = "~> 0.12.29"

  required_providers {
    google = "~> 3.31"
  }
}

provider "google" {
  credentials = file(var.GOOGLE_APPLICATION_CREDENTIALS)
  project = "four-track-friday-2"
  version = "~> 3.31"
}

resource "google_compute_global_address" "opening_hours_stage" {
  name = "oh-stg-ip"
  description = "a global ip address for the kubernetes load balancer"
  ip_version = "IPV4"
}

resource "google_compute_global_address" "opening_hours_prod" {
  name = "oh-prod-ip"
  description = "a global ip address for the kubernetes load balancer"
  ip_version = "IPV4"
}

resource "google_dns_managed_zone" "opening_hours_zone" {
  dns_name = "woltchallenge.app."
  name = "oh-zone"
}

resource "google_dns_record_set" "opening_hours_prod" {
  managed_zone = google_dns_managed_zone.opening_hours_zone.name
  name = google_dns_managed_zone.opening_hours_zone.dns_name
  rrdatas = [
    google_compute_global_address.opening_hours_prod.address]
  ttl = 300
  type = "A"
}

resource "google_dns_record_set" "opening_hours_stg" {
  managed_zone = google_dns_managed_zone.opening_hours_zone.name
  name = "stg.${google_dns_managed_zone.opening_hours_zone.dns_name}"
  rrdatas = [
    google_compute_global_address.opening_hours_stage.address]
  ttl = 300
  type = "A"
}

resource "google_dns_record_set" "opening_hours_prod_redirect" {
  managed_zone = google_dns_managed_zone.opening_hours_zone.name
  name = "www.${google_dns_managed_zone.opening_hours_zone.dns_name}"
  ttl = 300
  type = "CNAME"
  rrdatas = [
    google_dns_record_set.opening_hours_prod.name]
}

resource "google_storage_bucket" "static_content" {
  name = "static.woltchallenge.app"
  location = "us-west1"
  bucket_policy_only = true
}
