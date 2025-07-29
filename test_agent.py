#!/usr/bin/env python3
"""
Test script for the LangGraph Support Ticket Triage Agent

This script tests the implementation locally by invoking the compiled graph
with the evaluator input format to verify all nodes execute correctly.
"""

import sys
import traceback
from langchain_core.messages import HumanMessage

def test_agent():
    """Test the support ticket triage agent with sample tickets."""
    
    print("Testing LangGraph Support Ticket Triage Agent...")
    print("=" * 60)
    
    try:
        # Import the compiled graph
        from agent import app
        print("✅ Successfully imported compiled graph from agent.py")
        
        # Test cases with different ticket types and priorities
        test_cases = [
            {
                "name": "High Priority Billing Issue",
                "ticket": "URGENT: I was charged twice for my subscription this month and need an immediate refund. This is causing issues with my bank account."
            },
            {
                "name": "Technical Issue",
                "ticket": "The application keeps crashing when I try to upload files. I've tried restarting but the problem persists."
            },
            {
                "name": "General Inquiry",
                "ticket": "Hi, I'd like to know more about your premium features and pricing plans. Can someone help me understand the differences?"
            },
            {
                "name": "High Priority Technical Issue",
                "ticket": "CRITICAL: Our entire system is down and we can't access any of our data. This is an emergency situation affecting our business operations."
            },
            {
                "name": "Low Priority Billing Question",
                "ticket": "I have a question about my invoice from last month. Can you help me understand the charges?"
            }
        ]
        
        # Test each case
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n🧪 Test Case {i}: {test_case['name']}")
            print("-" * 40)
            print(f"Input: {test_case['ticket']}")
            
            try:
                # Create evaluator input format
                input_data = {"messages": [HumanMessage(content=test_case['ticket'])]}
                
                # Invoke the graph
                result = app.invoke(input_data)
                
                # Verify all required fields are present
                required_fields = ['category', 'priority', 'summary', 'email', 'acknowledgement']
                missing_fields = []
                
                for field in required_fields:
                    if field not in result or not result[field]:
                        missing_fields.append(field)
                
                if missing_fields:
                    print(f"❌ Missing required fields: {missing_fields}")
                else:
                    print("✅ All required fields present")
                    
                    # Display results
                    print(f"Category: {result.get('category', 'N/A')}")
                    print(f"Priority: {result.get('priority', 'N/A')}")
                    print(f"Summary: {result.get('summary', 'N/A')}")
                    print(f"Email: {result.get('email', 'N/A')}")
                    print(f"Acknowledgement: {result.get('acknowledgement', 'N/A')}")
                    
                    # Verify messages field
                    if 'messages' in result and len(result['messages']) > 0:
                        print(f"Messages count: {len(result['messages'])}")
                        print("✅ Messages field properly updated")
                    else:
                        print("❌ Messages field missing or empty")
                        
                    # Validate routing logic
                    category = result.get('category', '')
                    priority = result.get('priority', '')
                    email = result.get('email', '')
                    
                    expected_email = get_expected_email(category, priority)
                    if email == expected_email:
                        print("✅ Email routing is correct")
                    else:
                        print(f"❌ Email routing incorrect. Expected: {expected_email}, Got: {email}")
                
            except Exception as e:
                print(f"❌ Test failed with error: {str(e)}")
                print(f"Error type: {type(e).__name__}")
                traceback.print_exc()
                
        print("\n" + "=" * 60)
        print("Testing completed!")
        
    except ImportError as e:
        print(f"❌ Failed to import agent: {str(e)}")
        print("Make sure agent.py exists and has no syntax errors")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during testing: {str(e)}")
        traceback.print_exc()
        return False
    
    return True

def get_expected_email(category, priority):
    """Get the expected email address based on routing rules."""
    if category == "Billing":
        if priority == "High":
            return "priority-billing@company.com"
        else:
            return "billing@company.com"
    elif category == "Technical":
        if priority == "High":
            return "urgent-tech@company.com"
        else:
            return "tech@company.com"
    else:  # General Inquiry
        return "support@company.com"

def test_evaluator_format():
    """Test the exact evaluator input format."""
    print("\n🔍 Testing Evaluator Input Format")
    print("-" * 40)
    
    try:
        from agent import app
        
        # Test with minimal evaluator input
        evaluator_input = {"messages": [HumanMessage(content="My billing is wrong")]}
        
        print("Testing with evaluator input format:")
        print(f"Input: {evaluator_input}")
        
        result = app.invoke(evaluator_input)
        
        # Check that all state fields have values (not None or empty)
        required_fields = ['messages', 'category', 'priority', 'summary', 'email', 'acknowledgement']
        
        print("\nResult validation:")
        all_good = True
        for field in required_fields:
            if field in result and result[field]:
                print(f"✅ {field}: {result[field] if field != 'messages' else f'{len(result[field])} messages'}")
            else:
                print(f"❌ {field}: Missing or empty")
                all_good = False
        
        if all_good:
            print("\n✅ Evaluator format test PASSED")
        else:
            print("\n❌ Evaluator format test FAILED")
            
        return all_good
        
    except Exception as e:
        print(f"❌ Evaluator format test failed: {str(e)}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("LangGraph Support Ticket Triage Agent - Local Testing")
    print("=" * 60)
    
    # Run main tests
    success = test_agent()
    
    # Run evaluator format test
    evaluator_success = test_evaluator_format()
    
    if success and evaluator_success:
        print("\n🎉 All tests PASSED! The agent is ready for evaluation.")
        sys.exit(0)
    else:
        print("\n❌ Some tests FAILED. Please check the implementation.")
        sys.exit(1)
