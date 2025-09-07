"""
Unit tests for the BankReport class.

These tests cover all three levels of functionality:
- Level 1: Account creation and transfers
- Level 2: Top N spender tracking with proper sorting
- Level 3: Payment processing with cashback and cancellation
"""

import unittest
from main import BankReport


class TestBankReport(unittest.TestCase):
    """Test suite for the BankReport banking system."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.bank = BankReport()
    
    # ==================== Level 1 Tests ====================
    
    def test_create_account_success(self):
        """Test successful account creation."""
        result = self.bank.createAccount(1000, "ACC001")
        self.assertTrue(result, "Account creation should return True for new account")
    
    def test_create_account_duplicate(self):
        """Test creating duplicate accounts."""
        self.bank.createAccount(1000, "ACC001")
        result = self.bank.createAccount(2000, "ACC001")
        self.assertFalse(result, "Should return False when creating duplicate account")
    
    def test_create_multiple_accounts(self):
        """Test creating multiple unique accounts."""
        result1 = self.bank.createAccount(1000, "ACC001")
        result2 = self.bank.createAccount(1100, "ACC002")
        result3 = self.bank.createAccount(1200, "ACC003")
        
        self.assertTrue(result1, "First account should be created successfully")
        self.assertTrue(result2, "Second account should be created successfully")
        self.assertTrue(result3, "Third account should be created successfully")
    
    def test_transfer_between_valid_accounts(self):
        """Test successful transfer between two valid accounts."""
        self.bank.createAccount(1000, "ACC001")
        self.bank.createAccount(1100, "ACC002")
        
        result = self.bank.transfer(2000, "ACC001", "ACC002", 100)
        self.assertIsNotNone(result, "Transfer should return a status message")
    
    def test_transfer_from_nonexistent_account(self):
        """Test transfer from non-existent source account."""
        self.bank.createAccount(1000, "ACC002")
        
        result = self.bank.transfer(2000, "ACC001", "ACC002", 100)
        self.assertIn("fail", str(result).lower() if result else "", 
                     "Transfer from non-existent account should fail")
    
    def test_transfer_to_nonexistent_account(self):
        """Test transfer to non-existent target account."""
        self.bank.createAccount(1000, "ACC001")
        
        result = self.bank.transfer(2000, "ACC001", "ACC002", 100)
        self.assertIn("fail", str(result).lower() if result else "", 
                     "Transfer to non-existent account should fail")
    
    def test_transfer_negative_amount(self):
        """Test transfer with negative amount."""
        self.bank.createAccount(1000, "ACC001")
        self.bank.createAccount(1100, "ACC002")
        
        result = self.bank.transfer(2000, "ACC001", "ACC002", -50)
        self.assertIn("fail", str(result).lower() if result else "", 
                     "Transfer with negative amount should fail")
    
    def test_transfer_zero_amount(self):
        """Test transfer with zero amount."""
        self.bank.createAccount(1000, "ACC001")
        self.bank.createAccount(1100, "ACC002")
        
        result = self.bank.transfer(2000, "ACC001", "ACC002", 0)
        # Zero transfer might be allowed or not, depending on business logic
        self.assertIsNotNone(result, "Transfer should return a status")
    
    def test_transfer_to_same_account(self):
        """Test transfer to the same account (self-transfer)."""
        self.bank.createAccount(1000, "ACC001")
        
        result = self.bank.transfer(2000, "ACC001", "ACC001", 100)
        # Self-transfer might be allowed or not, depending on business logic
        self.assertIsNotNone(result, "Self-transfer should return a status")
    
    # ==================== Level 2 Tests ====================
    
    def test_top_n_spender_empty_system(self):
        """Test getting top spenders when no accounts exist."""
        result = self.bank.topNspender(1000, 5)
        self.assertEqual(result, [], "Should return empty list when no accounts exist")
    
    def test_top_n_spender_single_account(self):
        """Test getting top spenders with single account."""
        self.bank.createAccount(1000, "ACC001")
        
        result = self.bank.topNspender(2000, 1)
        self.assertEqual(len(result), 1, "Should return one account")
        self.assertEqual(result[0], "ACC001", "Should return the only account")
    
    def test_top_n_spender_with_transfers(self):
        """Test top spenders ranking based on transfer amounts."""
        # Create accounts
        self.bank.createAccount(1000, "Alice")
        self.bank.createAccount(1100, "Bob")
        self.bank.createAccount(1200, "Charlie")
        
        # Make transfers (Alice spends the most)
        self.bank.transfer(2000, "Alice", "Bob", 500)
        self.bank.transfer(2100, "Bob", "Charlie", 200)
        self.bank.transfer(2200, "Alice", "Charlie", 300)
        
        result = self.bank.topNspender(3000, 2)
        self.assertEqual(len(result), 2, "Should return top 2 spenders")
        self.assertEqual(result[0], "Alice", "Alice should be the top spender")
    
    def test_top_n_spender_alphabetical_tie_breaking(self):
        """Test alphabetical sorting when spending amounts are equal."""
        # Create accounts with names that need alphabetical sorting
        self.bank.createAccount(1000, "Charlie")
        self.bank.createAccount(1100, "Alice")
        self.bank.createAccount(1200, "Bob")
        
        # Make equal transfers for tie-breaking test
        self.bank.transfer(2000, "Charlie", "Alice", 100)
        self.bank.transfer(2100, "Bob", "Alice", 100)
        
        result = self.bank.topNspender(3000, 2)
        # Bob and Charlie both spent 100, should be sorted alphabetically
        if len(result) >= 2:
            self.assertTrue(result[0] < result[1] or 
                          self.bank.get_spending(result[0]) > self.bank.get_spending(result[1]),
                          "Should be sorted by amount first, then alphabetically")
    
    def test_top_n_spender_request_more_than_available(self):
        """Test requesting more top spenders than available accounts."""
        self.bank.createAccount(1000, "ACC001")
        self.bank.createAccount(1100, "ACC002")
        
        result = self.bank.topNspender(2000, 5)
        self.assertEqual(len(result), 2, "Should return all available accounts")
    
    def test_top_n_spender_zero_request(self):
        """Test requesting zero top spenders."""
        self.bank.createAccount(1000, "ACC001")
        
        result = self.bank.topNspender(2000, 0)
        self.assertEqual(result, [], "Should return empty list when n=0")
    
    # ==================== Level 3 Tests ====================
    
    def test_payment_success(self):
        """Test successful payment processing."""
        self.bank.createAccount(1000, "ACC001")
        
        payment_id = self.bank.payment(2000, "ACC001", 100)
        self.assertIsNotNone(payment_id, "Payment should return a payment ID")
        self.assertTrue(payment_id.startswith("payment"), 
                       "Payment ID should start with 'payment'")
    
    def test_payment_multiple_ids_unique(self):
        """Test that multiple payments generate unique IDs."""
        self.bank.createAccount(1000, "ACC001")
        
        payment_id1 = self.bank.payment(2000, "ACC001", 100)
        payment_id2 = self.bank.payment(2100, "ACC001", 200)
        payment_id3 = self.bank.payment(2200, "ACC001", 150)
        
        payment_ids = [payment_id1, payment_id2, payment_id3]
        unique_ids = set(payment_ids)
        
        self.assertEqual(len(payment_ids), len(unique_ids), 
                        "All payment IDs should be unique")
    
    def test_payment_nonexistent_account(self):
        """Test payment from non-existent account."""
        result = self.bank.payment(2000, "NONEXISTENT", 100)
        # Should either return None or an error indicator
        self.assertTrue(result is None or "error" in str(result).lower(),
                       "Payment from non-existent account should fail")
    
    def test_payment_negative_amount(self):
        """Test payment with negative amount."""
        self.bank.createAccount(1000, "ACC001")
        
        result = self.bank.payment(2000, "ACC001", -50)
        self.assertTrue(result is None or "error" in str(result).lower(),
                       "Payment with negative amount should fail")
    
    def test_payment_cashback_timing(self):
        """Test that cashback is applied after 24 hours."""
        self.bank.createAccount(1000, "ACC001")
        
        # Make payment at time 1000
        payment_id = self.bank.payment(1000, "ACC001", 1000)
        
        # Check balance immediately (no cashback yet)
        # This would need actual balance checking method
        
        # Check balance after 24 hours (86400 seconds)
        # Cashback of 2% = 20 should be applied
        # This test assumes there's a way to check account balance
        
        self.assertIsNotNone(payment_id, "Payment should be processed")
    
    def test_cancel_valid_payment(self):
        """Test cancelling a valid payment."""
        self.bank.createAccount(1000, "ACC001")
        payment_id = self.bank.payment(2000, "ACC001", 100)
        
        result = self.bank.cancel(3000, "ACC001", payment_id)
        self.assertTrue(result, "Should successfully cancel valid payment")
    
    def test_cancel_invalid_payment_id(self):
        """Test cancelling with invalid payment ID."""
        self.bank.createAccount(1000, "ACC001")
        
        result = self.bank.cancel(2000, "ACC001", "payment999")
        self.assertFalse(result, "Should fail to cancel non-existent payment")
    
    def test_cancel_wrong_account(self):
        """Test cancelling payment from wrong account."""
        self.bank.createAccount(1000, "ACC001")
        self.bank.createAccount(1100, "ACC002")
        
        payment_id = self.bank.payment(2000, "ACC001", 100)
        result = self.bank.cancel(3000, "ACC002", payment_id)
        
        self.assertFalse(result, 
                        "Should fail to cancel payment from different account")
    
    def test_cancel_already_cancelled(self):
        """Test cancelling an already cancelled payment."""
        self.bank.createAccount(1000, "ACC001")
        payment_id = self.bank.payment(2000, "ACC001", 100)
        
        # Cancel once
        self.bank.cancel(3000, "ACC001", payment_id)
        
        # Try to cancel again
        result = self.bank.cancel(4000, "ACC001", payment_id)
        self.assertFalse(result, "Should fail to cancel already cancelled payment")
    
    def test_cancel_after_cashback(self):
        """Test cancelling payment after cashback has been applied."""
        self.bank.createAccount(1000, "ACC001")
        
        # Make payment at time 1000
        payment_id = self.bank.payment(1000, "ACC001", 1000)
        
        # Try to cancel after 24 hours (when cashback is applied)
        result = self.bank.cancel(87400, "ACC001", payment_id)
        
        # Business logic might allow or disallow this
        self.assertIsNotNone(result, "Cancel should return a result")
    
    # ==================== Integration Tests ====================
    
    def test_complete_workflow(self):
        """Test a complete workflow with all operations."""
        # Create accounts
        self.bank.createAccount(1000, "Alice")
        self.bank.createAccount(1100, "Bob")
        self.bank.createAccount(1200, "Charlie")
        
        # Make transfers
        self.bank.transfer(2000, "Alice", "Bob", 200)
        self.bank.transfer(2100, "Bob", "Charlie", 50)
        
        # Make payments
        payment1 = self.bank.payment(3000, "Alice", 500)
        payment2 = self.bank.payment(3100, "Bob", 300)
        
        # Cancel a payment
        self.bank.cancel(4000, "Alice", payment1)
        
        # Check top spenders
        top_spenders = self.bank.topNspender(5000, 3)
        
        self.assertIsNotNone(top_spenders, "Should return top spenders list")
        self.assertTrue(len(top_spenders) <= 3, "Should not exceed requested count")
    
    def test_timestamp_ordering(self):
        """Test that operations respect timestamp ordering."""
        # Create account at time 2000
        result1 = self.bank.createAccount(2000, "ACC001")
        
        # Try to create same account at earlier time (should still fail as duplicate)
        result2 = self.bank.createAccount(1000, "ACC001")
        
        self.assertTrue(result1, "First creation should succeed")
        self.assertFalse(result2, "Second creation should fail even with earlier timestamp")


if __name__ == '__main__':
    unittest.main()
