#!/usr/bin/env python3
"""
Simple test runner for the tic-tac-toe BDD tests.
"""
import subprocess
import sys
import os

def run_bdd_tests():
    """Run the BDD tests using behave."""
    print("🎯 Running BDD Tests for Tic-Tac-Toe Game")
    print("=" * 50)
    
    # Change to the backend directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        # Run behave with verbose output
        result = subprocess.run(['behave', '-v'], capture_output=False)
        
        if result.returncode == 0:
            print("\n✅ All tests passed!")
            return True
        else:
            print("\n❌ Some tests failed!")
            return False
            
    except FileNotFoundError:
        print("❌ Error: 'behave' command not found. Please install behave:")
        print("   pip install behave")
        return False
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

if __name__ == "__main__":
    success = run_bdd_tests()
    sys.exit(0 if success else 1)