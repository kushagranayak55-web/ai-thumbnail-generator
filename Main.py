import sys
import platform

print("🐍 Python Health Check")
print("-" * 30)

print(f"Python version : {sys.version}")
print(f"Platform       : {platform.platform()}")
print(f"Python path    : {sys.executable}")

# Basic test
try:
    result = 10 + 20
    assert result == 30
    print("✅ Python execution: OK")
except Exception as e:
    print(f"❌ Python execution: FAILED - {e}")

# Import test
try:
    import os
    import json
    import math
    print("✅ Standard libraries: OK")
except Exception as e:
    print(f"❌ Standard libraries: FAILED - {e}")

print("-" * 30)
print("✅ Health check completed!")

