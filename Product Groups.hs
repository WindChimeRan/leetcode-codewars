-- https://www.codewars.com/kata/product-groups/train/haskell

module CodeWars.Group.Product where
import CodeWars.Group
import Data.Monoid

instance (Group a, Group b) => Group (a, b) where
    invert (x, y) = (invert x, invert y)
    
embedLeft :: (Group a, Group b) => a -> (a,b)
embedLeft x = (x, invert mempty)

embedRight :: (Group a, Group b) => b -> (a,b)
embedRight x = (invert mempty, x)
