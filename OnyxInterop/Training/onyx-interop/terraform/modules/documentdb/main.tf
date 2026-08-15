variable "environment" { type = string }
variable "project" { type = string }
variable "vpc_id" { type = string }
variable "subnet_ids" { type = list(string) }
variable "instance_class" { type = string }

resource "aws_docdb_subnet_group" "main" {
  name       = "${var.project}-${var.environment}-docdb"
  subnet_ids = var.subnet_ids
}

resource "aws_security_group" "docdb" {
  name        = "${var.project}-${var.environment}-docdb"
  description = "DocumentDB for Firely FHIR store"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 27017
    to_port     = 27017
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_docdb_cluster" "main" {
  cluster_identifier  = "${var.project}-${var.environment}-firely"
  engine              = "docdb"
  engine_version      = "5.0.0"
  master_username     = "firelyadmin"
  master_password     = "ChangeMeInSecretsManager!"
  db_subnet_group_name = aws_docdb_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.docdb.id]
  storage_encrypted   = true
  skip_final_snapshot = var.environment == "dev"
}

resource "aws_docdb_cluster_instance" "main" {
  count              = var.environment == "prod" ? 2 : 1
  identifier         = "${var.project}-${var.environment}-firely-${count.index + 1}"
  cluster_identifier = aws_docdb_cluster.main.id
  instance_class     = var.instance_class
}

output "cluster_endpoint" { value = aws_docdb_cluster.main.endpoint }
