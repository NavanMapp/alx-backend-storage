-- Create the index idx_name_first_score on the
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);
