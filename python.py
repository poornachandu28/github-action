name: Run Script

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - uses: jannekem/run-python-script-action@v1
        with:
          script: |
            import os
            print("Hello world")
            for f in os.listdir():
                print(f)
