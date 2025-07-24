#!/bin/bash

echo "🔍 NEXT.JS DIAGNOSTIC SCRIPT"
echo "=============================="

echo ""
echo "📋 System Information:"
echo "----------------------"
echo "Node.js version: $(node --version)"
echo "npm version: $(npm --version)"
echo "Operating System: $(uname -s)"
echo "Architecture: $(uname -m)"

echo ""
echo "💾 Memory Information:"
echo "---------------------"
if command -v free &> /dev/null; then
    free -h
else
    echo "Memory info not available on this system"
fi

echo ""
echo "📡 Active Node.js Processes:"
echo "-----------------------------"
if command -v ps &> /dev/null; then
    ps aux | grep node | grep -v grep || echo "No active Node.js processes found"
else
    echo "ps command not available"
fi

echo ""
echo "🌐 Port Information:"
echo "-------------------"
echo "Checking port 8000..."
if command -v lsof &> /dev/null; then
    lsof -i :8000 || echo "Port 8000 is free"
else
    echo "lsof command not available"
fi

echo ""
echo "🌐 Port 3000 Information:"
echo "------------------------"
echo "Checking port 3000..."
if command -v lsof &> /dev/null; then
    lsof -i :3000 || echo "Port 3000 is free"
else
    echo "lsof command not available"
fi

echo ""
echo "📦 Next.js Information:"
echo "----------------------"
npx next info

echo ""
echo "🔧 Project Dependencies:"
echo "-----------------------"
echo "Checking for heavy dependencies..."
npm list --depth=0 | grep -E "(react|next|@radix-ui)" | head -10

echo ""
echo "📁 Build Directory Status:"
echo "-------------------------"
if [ -d ".next" ]; then
    echo ".next directory exists"
    echo "Size: $(du -sh .next 2>/dev/null || echo 'Unable to calculate')"
else
    echo ".next directory does not exist"
fi

echo ""
echo "🧹 Cache Information:"
echo "--------------------"
if [ -d "node_modules/.cache" ]; then
    echo "Cache directory exists"
    echo "Size: $(du -sh node_modules/.cache 2>/dev/null || echo 'Unable to calculate')"
else
    echo "No cache directory found"
fi

echo ""
echo "⚡ Performance Recommendations:"
echo "------------------------------"
echo "1. Use 'npm run dev:safe' for lower memory usage"
echo "2. Use 'npm run dev:webpack' if turbopack causes issues"
echo "3. Run 'npm run clean' to clear caches"
echo "4. Use 'npm run build:analyze' to analyze bundle size"

echo ""
echo "🚀 Available Scripts:"
echo "-------------------"
npm run | grep -E "(dev|build|diagnose|clean|restart)"

echo ""
echo "✅ Diagnostic complete!"
