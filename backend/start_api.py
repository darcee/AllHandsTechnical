#!/usr/bin/env python3
"""
Startup script for the Tic-Tac-Toe FastAPI server.

This script starts the FastAPI server with appropriate configuration
for development and production environments.
"""

import uvicorn
import sys
import os

def main():
    """Start the FastAPI server."""
    print("🚀 Starting Tic-Tac-Toe Game API Server")
    print("=" * 50)
    
    # Configuration
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "true").lower() == "true"
    log_level = os.getenv("LOG_LEVEL", "info")

    print(f"📡 Server is listening on: http://localhost:{port}")
    print(f"📡 Server will start on: http://localhost:{port}")
    print(f"📚 API Documentation: http://localhost:{port}/docs")
    print(f"📖 ReDoc Documentation: http://localhost:{port}/redoc")
    print(f"🔄 Auto-reload: {reload}")
    print("=" * 50)
    
    try:
        uvicorn.run(
            "main:app",
            host=host,
            port=port,
            reload=reload,
            log_level=log_level,
            access_log=True
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()