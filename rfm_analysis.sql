-- ====================================================================
-- Project: ShopEase Customer Segmentation (RFM Model)
-- Description: Categorizes customers based on Recency, Frequency, and Monetary value to identify Champions and At-Risk segments.
-- ====================================================================

WITH rfm_base AS (
    SELECT 
        customer_id,
        MAX(order_date) AS last_purchase_date,
        COUNT(DISTINCT order_id) AS frequency,
        SUM(price * quantity) AS monetary_value
    FROM 
        cleaned_orders
    GROUP BY 
        customer_id
),
rfm_calc AS (
    SELECT 
        customer_id,
        -- Calculate Days Since Last Purchase (Assuming current date is '2024-01-01' for dataset context)
        EXTRACT(DAY FROM ('2024-01-01'::DATE - last_purchase_date)) AS recency,
        frequency,
        monetary_value
    FROM 
        rfm_base
),
rfm_scoring AS (
    SELECT 
        customer_id,
        NTILE(4) OVER (ORDER BY recency DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary_value ASC) AS m_score
    FROM 
        rfm_calc
)
-- Final Segmentation Logic
SELECT 
    customer_id,
    r_score,
    f_score,
    m_score,
    CONCAT(r_score, f_score, m_score) AS rfm_cell,
    CASE
        WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'Champion'
        WHEN r_score >= 3 AND f_score = 1 THEN 'Recent Customer'
        WHEN r_score <= 2 AND f_score >= 3 THEN 'At Risk (High Value)'
        WHEN r_score = 1 AND f_score = 1 THEN 'Lost'
        ELSE 'Regular Customer'
    END AS customer_segment
FROM 
    rfm_scoring
ORDER BY 
    monetary_value DESC;