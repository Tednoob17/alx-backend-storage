-- Creates an index idx_name_first on the table names & the 1st letter of n
CREATE INDEX idx_name_first ON names(name(1))
