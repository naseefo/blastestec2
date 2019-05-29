

subroutine mmult(C, A, B)
! =====================================================
! Uses the sieve of Eratosthenes to compute a logical
! array of size n_max, where .true. in element i
! indicates that i is a prime.
! =====================================================
    double precision, intent(in), dimension(6,6)   :: A
    double precision, intent(in), dimension(6,6)  :: B
    double precision, intent(out), dimension(6,6)  :: C

    integer :: i, j, k

    do i = 1, 6
        do j = 1, 6
            C(i,j) = 0.0
            do k = 1, 6
                C(i,j) = C(i,j) + A(i,k)*B(k,j)
            end do
        end do
    end do

    return
end subroutine mmult
