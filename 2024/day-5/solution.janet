(defn check-correctness
    "verify that the pageset is valid based on the ruleset"
    [pageset ruleset-table]

    (var ptr 0)
    # (prin "solving ")
    # (pp pageset)
    (var max (- (length pageset) 1))
    (var valid true)
    (var inx 0)
    # (pp ruleset-table)
    (while (< ptr max)
        (loop [i :range [ptr max]]
            (set inx (inc i))
            (var page-combo (string/join @[(pageset ptr) (pageset (inc i))] "|"))
            (var rev-page-combo (string/join @[(pageset (inc i)) (pageset ptr)] "|"))

            # (prin "checking for combo " page-combo " in ruleset:")
            # (pp  (get ruleset-table page-combo))
            (var combo-not-in-rulelist (nil? (get ruleset-table page-combo)))
            (var rev-combo-in-rulelist (not (nil? (get ruleset-table rev-page-combo))))
            (if (or combo-not-in-rulelist rev-combo-in-rulelist)
                (do 
                    (set valid false)
                    (break)
                )
            )
        )
        (if (not valid) (break))
        (set ptr (inc ptr))
    )
    [valid [ptr inx]]
)


(defn swap [tup a b]
    (def t (tup a))
    (put tup a (tup b))
    (put tup b t)
    )


(defn copy [arr]
    (var dup (array/new (length arr)))
    (loop [a :in arr] (array/push dup a))
    dup
    )

(defn solve [file-path]
    (var fl-rules-complete false)
    (var ruleset-table @{})
    (var pageset-list @[])
    (var file-lines (string/split "\n" (slurp file-path)))
    (loop [a :in file-lines]
        (var line-len (length a))
        (if (and (= 0 line-len) (not fl-rules-complete))
            (set fl-rules-complete true)
        )
        (if (not fl-rules-complete)
            (put ruleset-table a a) # if rules
            (do                     # if pages
                (def pset-list (string/split "," a))
                (if (< 1 (length pset-list))
                    (set pageset-list (array/push pageset-list pset-list))
                )
            )
        )
    )

    # (pp ruleset-table)
    (var valid-count 0)
    (var invalid-count 0)
    (loop [pset :in pageset-list]
        (var pset-list (copy pset))
        (var mid (math/floor (/ (length pset-list) 2)))
        (var res (check-correctness pset-list ruleset-table))
        # (pp res)
        (var valid (res 0))
        (var [ptr inx] (res 1))
        (if valid
            # if true:
            (set valid-count (+ valid-count (int/s64 (in pset-list mid))))
            # if false
            (do 
                (while (not valid)
                    (set pset-list (swap pset-list ptr inx))                             # swap the mismatched set
                    (var res (check-correctness pset-list ruleset-table))     # check if correct
                    (if (res 0)
                        (do                          # if true, exit loop
                            (set valid (res 0))
                            (break)
                            )
                        (do                          # if false, loop again
                            (set ptr ((res 1) 0))
                            (set inx ((res 1) 1))
                        )
                    )
                )
                (set invalid-count (+ invalid-count (int/s64 (in pset-list mid))))
                )
            )
        )
    (print "Final valid count is " valid-count)
    (print "Final invalid count is " invalid-count)
    )
(solve "input.txt")
