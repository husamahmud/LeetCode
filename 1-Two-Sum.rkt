(define/contract (create-assocs nums target count)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof pair?))
  (cond
    [(empty? nums) empty]
    [else (cons (cons (- target (first nums)) count) (create-assocs (rest nums) target (add1 count)))]))

(define/contract (find-pair nums count ht)
  (-> (listof exact-integer?) exact-integer? hash? (listof exact-integer?))
  (cond
    [(empty? nums) empty]
    [(and (hash-has-key? ht (first nums)) (not (= (hash-ref ht (first nums)) count))) 
        (list (hash-ref ht (first nums)) count)]
    [else (find-pair (rest nums) (add1 count) ht)]))


(define/contract (two-sum nums target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ([ht (make-hash (create-assocs nums target 0))])
    (find-pair nums 0 ht)))