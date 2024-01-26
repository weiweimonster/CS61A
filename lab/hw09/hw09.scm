(define-macro (switch expr cases)
  (cons 'cond
        (map (lambda  (case)
                        (cons (eq? (eval expr) (car case)) (cdr case)))
             cases)))
