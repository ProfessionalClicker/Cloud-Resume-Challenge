.PHONY: build

build:
	sam build

deploy-infra:
	sam build && sam deploy

deploy-site:
	aws s3 sync ./resume-site s3://crc-website --delete

invoke-views:
	sam build && sam local invoke HelloWorldFunction