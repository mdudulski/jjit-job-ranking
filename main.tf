provider "google" {

  project     = "jjit-job-ranking"
  credentials = "${file("credentials.json")}"
  region      = "us-central1"
  zone        = "us-central1-a"
}

resource "google_compute_instance" "my-instance" {
  name                      = "jj-cp1"
  machine_type              = "f1-micro"
  zone                      = "us-central1-a"
  allow_stopping_for_update = true

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"
    access_config {
      //neccesary event empty
    }
  }
}
