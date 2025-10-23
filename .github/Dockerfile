FROM rust:1.85.0-bookworm AS builder

WORKDIR /app

COPY Cargo.toml Cargo.lock ./
COPY simeis-data ./simeis-data
COPY simeis-server ./simeis-server

RUN cargo build --release --bin simeis-server

FROM debian:bullseye-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Copy the binary from builder
COPY --from=builder /app/target/release/simeis-server /app/simeis-server

# Expose the port
EXPOSE 8080

# Run the server
CMD ["/app/simeis-server"]
