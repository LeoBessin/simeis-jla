FROM rust:1.75
WORKDIR /app
COPY . .
RUN cargo build
RUN cargo run