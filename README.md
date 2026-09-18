# AWS EKS + ArgoCD GitOps Platform

A hands-on DevOps project demonstrating a complete CI/CD and GitOps workflow using AWS EKS, Terraform, Docker, Amazon ECR, GitHub Actions, Helm, and ArgoCD.

## Architecture

Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI
    |
    +--> Test Flask Application
    +--> Build Docker Image
    +--> Authenticate to AWS using OIDC
    +--> Push Image to Amazon ECR
    |
    v
Helm Desired State in Git
    |
    v
ArgoCD
    |
    v
Amazon EKS
    |
    v
Flask Application

## Technologies Used

- AWS EKS
- Amazon ECR
- AWS IAM / GitHub OIDC
- Terraform
- Kubernetes
- Docker
- GitHub Actions
- Helm
- ArgoCD
- Python / Flask
- Git

## Infrastructure

Terraform provisions:

- Custom AWS VPC
- Two public subnets across Availability Zones
- Internet Gateway
- Route table
- Amazon EKS cluster
- EKS managed node group
- IAM roles and policies

The infrastructure is defined as code inside the `terraform/` directory.

## Continuous Integration

GitHub Actions automatically:

1. Checks out the source code.
2. Installs Python dependencies.
3. Tests the Flask application.
4. Builds a Docker image.
5. Authenticates to AWS using GitHub OIDC.
6. Logs into Amazon ECR.
7. Tags the image using the Git commit SHA.
8. Pushes the image to Amazon ECR.

Using OIDC avoids storing long-lived AWS access keys in GitHub.

## Helm

The Flask application is packaged using a Helm chart.

The chart defines:

- Kubernetes Deployment
- Kubernetes Service
- Container image
- Resource requests and limits
- Readiness probe
- Liveness probe

## GitOps with ArgoCD

ArgoCD monitors the GitHub repository and uses:

`helm/flask-app`

as the application's desired state.

Automated synchronization is enabled with:

- Self-healing
- Automatic synchronization
- Resource pruning

When the image tag in Git changes, ArgoCD detects the new desired state and synchronizes the EKS cluster.

## End-to-End Deployment

The project successfully demonstrated:

Code Change
→ Git Push
→ GitHub Actions
→ Docker Build
→ Amazon ECR
→ Helm Desired State
→ ArgoCD
→ Amazon EKS
→ Running Application

Final application test:

```text
Symon's EKS GitOps Deployment

Deployed successfully with GitHub Actions, Amazon ECR, Helm and ArgoCD!

Version: v2
