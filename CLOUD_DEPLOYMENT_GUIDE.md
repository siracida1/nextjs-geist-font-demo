# 🚀 Next.js Cloud Deployment & Troubleshooting Guide

## 📋 Quick Solutions for Development Server Issues

### 1. Memory-Optimized Commands

```bash
# Standard development (4GB memory limit)
npm run dev

# Safe mode (2GB memory limit for constrained environments)
npm run dev:safe

# Webpack fallback (if turbopack causes issues)
npm run dev:webpack

# Clean restart (clears all caches)
npm run restart
```

### 2. Diagnostic Commands

```bash
# Run comprehensive diagnostics
npm run diagnose

# Or run the script directly
./scripts/diagnose.sh

# Check specific issues
npx next info
lsof -i :8000  # Check port usage
free -m        # Check memory usage
```

## 🔧 Cloud Environment Optimizations

### For Blackbox AI and Similar Platforms

#### Environment Variables
Add these to your cloud environment:

```bash
NODE_OPTIONS="--max_old_space_size=4096"
PORT=8000
NODE_ENV=development
NEXT_TELEMETRY_DISABLED=1
```

#### Memory Limits
- **Development**: 4GB (`--max_old_space_size=4096`)
- **Build**: 6GB (`--max_old_space_size=6144`)
- **Safe Mode**: 2GB (`--max_old_space_size=2048`)

### Docker Deployment

```bash
# Build Docker image
docker build -t nextjs-app .

# Run with memory limits
docker run -p 8000:8000 --memory=4g nextjs-app
```

## 🐛 Common Issues & Solutions

### Issue 1: "JavaScript heap out of memory"

**Solutions:**
```bash
# Increase memory limit
NODE_OPTIONS="--max_old_space_size=6144" npm run build

# Use safe mode
npm run dev:safe

# Clear caches
npm run clean
```

### Issue 2: Port 8000 already in use

**Solutions:**
```bash
# Kill process using port 8000
fuser -k 8000/tcp

# Or find and kill specific process
lsof -i :8000
kill -9 <PID>

# Use alternative port
PORT=3001 npm run dev
```

### Issue 3: Turbopack issues in cloud

**Solutions:**
```bash
# Disable turbopack
npm run dev:webpack

# Or modify next.config.ts
# experimental: { turbopack: false }
```

### Issue 4: Heavy dependencies causing slowdown

**Solutions:**
```bash
# Analyze bundle size
npm run build:analyze

# Check dependency sizes
npm list --depth=0

# Consider dynamic imports for heavy components
```

## 📊 Bundle Analysis

### Analyze Your Bundle
```bash
# Generate bundle analysis
ANALYZE=true npm run build

# This will open a web interface showing:
# - Bundle sizes
# - Duplicate dependencies
# - Optimization opportunities
```

### Heavy Dependencies in Your Project
- `@radix-ui/*` components: ~2MB
- `recharts`: ~500KB
- `lucide-react`: ~300KB
- `date-fns`: ~200KB

## 🎯 Performance Optimizations

### 1. Dynamic Imports
```tsx
// Instead of static imports
import { Chart } from '@/components/ui/chart'

// Use dynamic imports for heavy components
const Chart = dynamic(() => import('@/components/ui/chart'), {
  ssr: false,
  loading: () => <div>Loading chart...</div>
})
```

### 2. Code Splitting
Your `next.config.ts` is configured to:
- Split vendor chunks
- Separate UI library chunks
- Optimize package imports

### 3. Image Optimization
- WebP format enabled
- Multiple device sizes configured
- Lazy loading by default

## 🔄 Troubleshooting Workflow

### Step 1: Run Diagnostics
```bash
npm run diagnose
```

### Step 2: Check Memory Usage
```bash
# Linux/Mac
free -m
top -p $(pgrep node)

# Check Node.js memory in browser console
console.log(performance.memory)
```

### Step 3: Try Safe Mode
```bash
npm run dev:safe
```

### Step 4: Clear Everything
```bash
npm run clean
npm install
npm run dev
```

### Step 5: Use Webpack Fallback
```bash
npm run dev:webpack
```

## 🌐 Cloud Platform Specific

### Blackbox AI
- Use `NODE_OPTIONS` environment variable
- Enable standalone output mode
- Use port 8000 (configured in package.json)

### Vercel
```bash
# Deploy with optimizations
vercel --prod
```

### Railway
```json
// railway.json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "npm start",
    "healthcheckPath": "/api/health"
  }
}
```

### Render
```yaml
# render.yaml
services:
  - type: web
    name: nextjs-app
    env: node
    buildCommand: npm run build
    startCommand: npm start
    envVars:
      - key: NODE_OPTIONS
        value: "--max_old_space_size=4096"
```

## 📈 Monitoring & Debugging

### Memory Monitoring
```tsx
// Add to your component
import { getMemoryUsage } from '@/lib/memory-utils'

useEffect(() => {
  const memory = getMemoryUsage()
  if (memory) {
    console.log('Memory usage:', memory)
  }
}, [])
```

### Performance Monitoring
```tsx
// Add performance marks
performance.mark('component-start')
// ... component logic
performance.mark('component-end')
performance.measure('component-time', 'component-start', 'component-end')
```

## 🆘 Emergency Solutions

### If Nothing Works:

1. **Minimal Setup**:
   ```bash
   # Create new Next.js app
   npx create-next-app@latest minimal-test
   cd minimal-test
   npm run dev
   ```

2. **Gradual Migration**:
   - Copy components one by one
   - Test after each addition
   - Identify problematic dependencies

3. **Alternative Approaches**:
   - Use Vite instead of Next.js
   - Consider server-side rendering alternatives
   - Split into micro-frontends

## 📞 Support Resources

- Next.js Documentation: https://nextjs.org/docs
- Vercel Support: https://vercel.com/support
- GitHub Issues: https://github.com/vercel/next.js/issues

---

**Last Updated**: $(date)
**Next.js Version**: 15.3.2
**Node.js Recommended**: 18.x or 20.x
