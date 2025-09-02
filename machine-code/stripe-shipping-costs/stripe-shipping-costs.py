'''
Question: Shipping Cost with Quantity (Edited with DeepSeek)
We have:
Orders - containing items with quantities (e.g., 20 mice, 5 laptops)
Shipping Cost Rules - that determine how much it costs to ship these items, which can vary by:
Country (US vs CA)
Product type (mouse vs laptop)
Quantity ordered
Pricing type (fixed vs incremental)
Part 1: Simple Fixed Cost Calculation
In the first scenario (demo_shipping_cost), each product has a fixed cost per unit regardless of quantity:
US: $550/mouse, $1000/laptop
CA: $750/mouse, $1100/laptop
Calculation Example for US Order:
20 mice × $550 = $11,000
5 laptops × $1000 = $5,000
Total = $16,000
Part 2: Tiered Quantity Pricing
In the second scenario, costs change based on quantity thresholds:
For laptops in US:
First 2 units: $1000 each
3rd unit and beyond: $900 each
Calculation Example for US Order (5 laptops):
First 2 laptops: 2 × $1000 = $2000
Next 3 laptops: 3 × $900 = $2700
Total laptop shipping = $4700 (Mice remain $550 each regardless of quantity)
Part 3: Mixed Pricing Types (Fixed vs Incremental)
This is the most complex scenario:
Fixed Cost: You pay the full amount if you order ANY quantity in that range.
Incremental Cost: You pay per unit like before.
Key Differences:
For a "fixed" cost tier:
If you order 1 laptop in 0-2 range, you pay $1000 (not $1000 × quantity).
If you order 2 laptops, still just $1000 total.
For "incremental", it works like Part 2 (cost × quantity).
Calculation Example for US Order (5 laptops):
First tier (0-2 units, fixed cost):
Since we have 5 laptops, we qualify for this tier.
Pay the fixed $1000 once (regardless of whether it's 1 or 2 laptops).
Second tier (3+, incremental cost):
We have 3 laptops in this tier (5 total - 2 from first tier).
Pay 3 × $900 = $2700
Total laptop shipping = $1000 + $2700 = $3700 (Compared to $4700 in Part 2)
Key Points to Notice:
The major difference is how "fixed" costs behave - you pay the amount once for the entire quantity range, while "incremental" costs multiply by quantity.
For mice, since there's only one tier with incremental pricing, it behaves the same in all scenarios.
The most complex case is when you have mixed fixed and incremental costs for the same product.

'''