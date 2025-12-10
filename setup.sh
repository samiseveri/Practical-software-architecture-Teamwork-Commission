#!/usr/bin/env bash
set -e

echo "=== CLEAN SETUP: Creating NestJS + Prisma Backend ==="

PROJECT="price-checker-backend"

# Delete old folder if exists
rm -rf "$PROJECT"

# Create new project folder
mkdir -p "$PROJECT"
cd "$PROJECT"

# Initialize Nest project
npm init -y
npm install -g @nestjs/cli
nest new . --skip-git --skip-install --package-manager npm

echo "Installing core dependencies..."
npm install @nestjs/config @nestjs/jwt @nestjs/passport bcrypt @prisma/client prisma

echo "Installing dev dependencies..."
npm install -D @types/bcrypt @types/node

echo "Creating folder structure..."
mkdir -p prisma
mkdir -p src/modules/{auth,users,store,prices}

echo "Writing Prisma schema..."
cat <<EOF > prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id       Int    @id @default(autoincrement())
  email    String @unique
  password String
  role     String
}

model Store {
  id        Int      @id @default(autoincrement())
  name      String
  latitude  Float
  longitude Float
  prices    Price[]
}

model Price {
  id         Int      @id @default(autoincrement())
  gtin       String
  barcode    String
  price      Float
  timestamp  DateTime @default(now())
  storeId    Int
  store      Store    @relation(fields: [storeId], references: [id])
}
EOF

echo "Creating .env file..."
cat <<EOF > .env
DATABASE_URL="postgresql://user:password@localhost:5432/pricechecker"
JWT_SECRET="secret"
PORT=3000
EOF

echo "=== CLEAN BACKEND GENERATED SUCCESSFULLY ==="
echo "Next steps:"
echo "1. Start PostgreSQL"
echo "2. Run: npx prisma migrate dev --name init"
echo "3. Run: npm run start:dev"

