# Basic Biometric Template Protection (BTP) Scheme

## Overview
Biometric Template Protection (BTP) is an important component in biometric systems, aimed at protecting sensitive biometric data from being compromised. However, BTP can often be a complex topic difficult to understand for beginners. This repository provides a **basic and simplified implementation** of a BTP scheme for **educational purposes**. 

My goal is to demonstrate the fundamental concepts of template protection using a simple cryptographic technique, rather than creating a production ready system designed for secure deployment.

## How it Works

This simplified scheme consists of two main phases: **Enrollment** and **Authentication**.

### Enrollment
1. The biometric data (represented as an embedding `emb1`) is first quantized into a binary vector (`vec1`).
2. A `secret_key` is generated, which is a random binary vector of the same length as `vec1`.
3. The client then encrypts the binarized template by XORing `vec1` with the `secret_key` to create `encrypted_vec1`.
4. The client stores the `secret_key` and sends `encrypted_vec1` to the server for later authentication.

### Authentication
1. During authentication, a new biometric sample (`emb2`) is captured and quantized to `vec2`.
2. The client XORs `vec2` with the stored `secret_key` to create `encrypted_vec2`.
3. The server calculates the **Hamming distance** between `encrypted_vec1` (from enrollment) and `encrypted_vec2` (from authentication).
4. If the Hamming distance is below a certain threshold, the user is authenticated.

![Scheme Diagram](Images/Scheme_Diagram.png)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/templateprotection/basic-btp.git
   cd btp-scheme
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the code:
   ```bash
   python btp.py
   ```
