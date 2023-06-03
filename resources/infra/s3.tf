# Create an S3 bucket for storing files
resource "aws_s3_bucket" "my_bucket" {
  bucket = "cloud-hippie-homebrew"
  acl    = "private"
}

