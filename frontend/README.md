# 🎮 Tic-Tac-Toe Frontend

React + TypeScript + Vite frontend for the Tic-Tac-Toe game API.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linting
npm run lint

# Type checking
npm run type-check
```

## 🔧 Development Setup

### Prerequisites
- Node.js 18+ 
- npm or yarn
- Backend API running on `http://localhost:8000`

### Configuration

The frontend is configured to:
- Run on port `54281` (as specified in runtime requirements)
- Proxy API requests from `/api/*` to `http://localhost:8000`
- Support hot module replacement (HMR)
- Include TypeScript type checking

### Project Structure

```
frontend/
├── src/
│   ├── components/     # React components (to be created)
│   ├── hooks/         # Custom React hooks (to be created)
│   ├── types/         # TypeScript type definitions (to be created)
│   ├── services/      # API service functions (to be created)
│   ├── App.tsx        # Main App component
│   └── main.tsx       # Entry point
├── public/            # Static assets
├── package.json       # Dependencies and scripts
├── vite.config.ts     # Vite configuration
└── tsconfig.json      # TypeScript configuration
```

## 🔗 API Integration

The frontend connects to the backend API through:
- **Proxy Configuration**: `/api/*` routes proxy to `http://localhost:8000`
- **CORS Support**: Backend configured to allow frontend requests
- **Type Safety**: TypeScript interfaces for API responses

## 🛠️ Tech Stack

- **React 19** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **ESLint** - Code linting
- **CSS Modules** - Styling (ready to use)

## 📝 Next Steps

Ready for implementation of:
- Game board component
- Player management
- Game state management
- Real-time updates
- Responsive design