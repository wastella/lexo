#!/usr/bin/env python3
import argparse
from lexo.lexo import Learner
from lexo.A1_concepts import spanish_a1_concepts

def main():
    parser = argparse.ArgumentParser(description='Lexo - Language Learning CLI')
    parser.add_argument('-k', '--key', required=True, help='Google Gemini API key')
    parser.add_argument('-f', '--file', help='Path to save/load progress (default: stored_concepts.json)')
    parser.add_argument('-n', '--num-sessions', type=int, default=3,
                       help='Number of practice sessions to run (default: 3)')
    args = parser.parse_args()

    print("Welcome to Lexo! Starting a new practice session...")
    
    # Initialize learner with concepts and API key
    learner = Learner(spanish_a1_concepts, args.key, args.file) if args.file else Learner(spanish_a1_concepts, args.key)
    
    try:
        sessions_completed = 0
        while sessions_completed < args.num_sessions:
            # Practice one concept
            if not learner.practice():  # Returns False if no more concepts
                break
                
            sessions_completed += 1
            
            # If we haven't reached the session limit, ask to continue
            if sessions_completed < args.num_sessions:
                response = input("\nContinue to next session? (y/n): ").lower()
                if response != 'y':
                    break
                    
    except KeyboardInterrupt:
        print("\nSaving progress...")
    finally:
        # Always save progress when exiting
        learner.save()
        print(f"Progress saved to {learner.session_file}. Goodbye!")

if __name__ == "__main__":
    main()