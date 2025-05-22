provider "aws" {
  region = "eu-central-1"
}

resource "aws_iam_role" "github_actions_oidc" {
  name = "github-actions-oidc-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Federated = "arn:aws:iam::<YOUR_AWS_ACCOUNT_ID>:oidc-provider/token.actions.githubusercontent.com"
      },
      Action = "sts:AssumeRoleWithWebIdentity",
      Condition = {
        StringLike = {
          "token.actions.githubusercontent.com:sub" = "repo:<YOUR_GITHUB_USER>/gpt-pipeline-hub:*"
        }
      }
    }]
  })
}

resource "aws_iam_policy" "github_ci_permissions" {
  name = "github-actions-deploy-permissions"
  path = "/"
  description = "Permissions for GitHub Actions to access ECR and ECS"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "ecr:GetAuthorizationToken",
          "ecr:BatchCheckLayerAvailability",
          "ecr:PutImage",
          "ecr:InitiateLayerUpload",
          "ecr:UploadLayerPart",
          "ecr:CompleteLayerUpload",
          "ecr:BatchGetImage"
        ],
        Resource = "*"
      },
      {
        Effect = "Allow",
        Action = [
          "ecs:UpdateService",
          "ecs:DescribeServices",
          "ecs:DescribeTaskDefinition",
          "ecs:RegisterTaskDefinition"
        ],
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "github_ci_attach" {
  role       = aws_iam_role.github_actions_oidc.name
  policy_arn = aws_iam_policy.github_ci_permissions.arn
}
