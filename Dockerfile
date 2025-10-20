ARG RUST_VERSION=1.90.0
FROM rust:${RUST_VERSION}-slim-bullseye
WORKDIR /
COPY . .
RUN cargo build