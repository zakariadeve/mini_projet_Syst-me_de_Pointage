#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to reset the database - with force close"""

import os
import sys
import gc

# Force garbage collection to close any open handles
gc.collect()

# Remove old database with retry
db_path = "etudiants.db"
max_retries = 3
for attempt in range(max_retries):
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            print(f"[OK] Old database removed: {db_path}")
            break
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"[WARN] Attempt {attempt + 1} failed, retrying...")
                import time
                time.sleep(0.5)
            else:
                print(f"[ERR] Failed to remove database after {max_retries} attempts: {e}")

# Import app and recreate database
try:
    from app import app, db, Etudiant
    from datetime import datetime
    
    with app.app_context():
        # Close any existing connections
        db.engine.dispose()
        
        # Drop all tables first (if possible)
        try:
            db.drop_all()
            print("[OK] Old tables dropped")
        except:
            pass
        
        # Create all tables fresh
        db.create_all()
        print("[OK] Database schema created")
        
        # Add a test record
        test = Etudiant(
            nom="Test User",
            heure="10:00:00",
            date=datetime.now().date(),
            statut="Présent"
        )
        db.session.add(test)
        db.session.commit()
        
        # Verify
        count = Etudiant.query.count()
        print(f"[OK] Database initialized with {count} test record")
        
except Exception as e:
    print(f"[ERR] Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("[OK] Database ready for use")
