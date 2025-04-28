# gihub-actions-self-hosted-ecr-image

A minimal Python project demonstrating Docker best practices, GitHub Actions self hosted runner, and secure dependency management using [uv package manager](https://docs.astral.sh/uv/).

## Project Structure

- `calculator.py` — Main application logic
- `test_calculator.py` — Unit tests for the calculator
- `pyproject.toml` — Project metadata and dependencies
- `uv.lock` — Lockfile for reproducible installs
- `Dockerfile` — Containerization with security best practices

## CI/CD on EC2 Self-Hosted Runner

This project is designed to run on an **EC2 instance** using a self-hosted GitHub Actions runner.  
See [`.github/workflows/ci-self-hosted.yml`](.github/workflows/ci-self-hosted.yml) for the workflow configuration.

## Local Development Steps

1. **Install [uv](https://github.com/astral-sh/uv) and check version:**
   ```sh
   pip3 install uv
   uv --version
   ```
2. **Create and activate a virtual environment:**
   ```sh
   uv venv
   source .venv/bin/activate
   ```
3. **Add and install test dependencies:**
   ```sh
   uv add pytest
   ```
4. **Run the app locally:**
   ```sh
   uv run calculator.py
   ```
5. **Run test cases locally:**
   ```sh
   python3 -m pytest -vs test_calculator.py
   ```

## Docker Usage

1. **Build the image:**
   ```sh
   docker build -t gh-actions-self-hosted-calc-app .
   ```
2. **Run the container (listening on port 8080):**
   ```sh
   docker run -p 8080:8080 gh-actions-self-hosted-calc-app
   ```

## Docker Build and Push to AWS ECR

The following steps (see [ci-self-hosted.yml](.github/workflows/ci-self-hosted.yml)) are used to build and push the Docker image to AWS ECR:

```sh
# Authenticate Docker to your ECR registry
aws ecr get-login-password --region <AWS_REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com

# Build the Docker image with a tag (e.g., short SHA and date)
SHORT_SHA=$(echo $GITHUB_SHA | tail -c 6)
TAG_DATE=$(date +"%d-%b-%y")
IMAGE_TAG="${SHORT_SHA}-${TAG_DATE}"
docker build . --file Dockerfile --tag <ECR_REGISTRY>/<ECR_REPOSITORY>:${IMAGE_TAG}

# Push the image to ECR
docker push <ECR_REGISTRY>/<ECR_REPOSITORY>:${IMAGE_TAG}
```

## Security Best Practices
- Uses a non-root user in Docker
- Only exposes necessary ports
- Uses `uv` for secure, reproducible dependency management
- Keeps dependencies and code separate for better caching

---

MIT License