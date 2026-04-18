-- 1. Pattern Search Function
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(search_pattern TEXT)
RETURNS TABLE (
    id INT,
    f_name VARCHAR,
    l_name VARCHAR,
    p_number VARCHAR
) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    WHERE first_name ILIKE '%' || search_pattern || '%'
       OR last_name ILIKE '%' || search_pattern || '%'
       OR phone_number ILIKE '%' || search_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 4. Pagination Function
CREATE OR REPLACE FUNCTION get_contacts_paged(p_limit INT, p_offset INT)
RETURNS TABLE (
    id INT,
    f_name VARCHAR,
    l_name VARCHAR,
    p_number VARCHAR
) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    ORDER BY contact_id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;