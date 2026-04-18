-- 2. Upsert Procedure (Insert or Update)
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_phone VARCHAR
) AS $$
BEGIN
    INSERT INTO phonebook (first_name, last_name, phone_number)
    VALUES (p_first_name, p_last_name, p_phone)
    ON CONFLICT (first_name, last_name) 
    DO UPDATE SET phone_number = EXCLUDED.phone_number;
END;
$$ LANGUAGE plpgsql;

-- 5. Delete Procedure
CREATE OR REPLACE PROCEDURE delete_contact(p_identifier VARCHAR)
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE first_name = p_identifier 
       OR phone_number = p_identifier;
END;
$$ LANGUAGE plpgsql;

-- 3. Bulk Insert with Validation
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names VARCHAR[], 
    p_phones VARCHAR[],
    OUT o_invalid_data VARCHAR[]
) AS $$
DECLARE
    i INT;
BEGIN
    o_invalid_data := ARRAY[]::VARCHAR[];
    FOR i IN 1 .. array_length(p_names, 1) LOOP
        -- Simple validation: Phone must be digits and length 7-15
        IF p_phones[i] ~ '^[0-9]{7,15}$' THEN
            INSERT INTO phonebook (first_name, phone_number) 
            VALUES (p_names[i], p_phones[i]);
        ELSE
            o_invalid_data := array_append(o_invalid_data, p_names[i] || ':' || p_phones[i]);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;