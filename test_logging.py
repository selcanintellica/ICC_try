"""
Simple test to verify logging is working.
Run this to check if logs appear in your terminal.
"""
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

logger = logging.getLogger(__name__)

print("\n" + "="*60)
print("🧪 LOGGING TEST")
print("="*60)

print("\n✅ This is a PRINT statement - you should see this")
logger.info("✅ This is a LOGGER.INFO - you should see this too")
logger.debug("🔍 This is a LOGGER.DEBUG - you WON'T see this (level=INFO)")
logger.warning("⚠️ This is a LOGGER.WARNING - you should see this")
logger.error("❌ This is a LOGGER.ERROR - you should see this")

print("\n" + "="*60)
print("If you see all the messages above, logging is working!")
print("="*60 + "\n")
