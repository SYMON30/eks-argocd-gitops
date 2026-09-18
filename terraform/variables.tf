variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-3"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "eks-argocd-gitops"
}
