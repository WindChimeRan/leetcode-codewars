module Diff (sumOfDifferences) where

sumOfDifferences :: [Int] -> Maybe Int
sumOfDifferences [] = Nothing
sumOfDifferences [_] = Nothing
sumOfDifferences xs = Just $ maximum xs - minimum xs
