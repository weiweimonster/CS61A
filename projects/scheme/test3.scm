(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))

(define define? (check-special 'define))

(define quoted? (check-special 'quote))

(define let? (check-special 'let))

(define (caar x) (car (car x)))

(define (zip pairs)
  (list (map car pairs) (map cadr pairs)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))

(define (let-to-lambda expr)
  (cond 
    ((atom? expr)
     ; BEGIN PROBLEM 17
     expr
     ; END PROBLEM 17
    )
    ((quoted? expr)
     ; BEGIN PROBLEM 17
     expr
     ; END PROBLEM 17
    )
    ((or (lambda? expr) (define? expr))
     (let ((form (car expr))
           (params (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM 17
       (cons form (cons params (map let-to-lambda body)))
       ; END PROBLEM 17
     ))
    ((let? expr)
     (let ((values (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM 17
       (cons (cons 'lambda
                   (cons (car (zip values)) (map let-to-lambda body)))
             (map let-to-lambda (cadr (zip values))))
       ; END PROBLEM 17
     ))
    (else
     ; BEGIN PROBLEM 17
     (cons (car expr) (map let-to-lambda (cdr expr)))
     ; END PROBLEM 17
    )))

(let-to-lambda '(let
                 ((a
                   (let
                    ((a
                      2))
                    a))
                  (b
                   2))
                 (+
                  a
                  b)))
