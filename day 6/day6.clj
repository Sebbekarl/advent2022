
(->> (slurp "C:/Users/sebastian/Documents/c programmering/advent/day 6/input.txt")
     (partition 4 1)
     (map (comp count set))
     (map-indexed vector)
     (filter (fn [[_ unique_chars]] (= unique_chars 4))) 
     )

(->> (slurp "C:/Users/sebastian/Documents/c programmering/advent/day 6/input.txt")
     (partition 14 1)
     (map (comp count set))
     (map-indexed vector)
     (filter (fn [[_ unique_chars]] (= unique_chars 14))))

  

