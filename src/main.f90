module helper

   implicit none
!~ 	private
!~ 	public  :: lomb2, lomb3

contains

   function lomb3_difftimes(time, thetas, phis, sigs, m, n, f) result(p)
!~ 	   Calculates the Lomb periodogram with spatial dependencies given by the angles
!~      thetas and phis, for mode number m, n, and frequency f.
!~       In contrast to "lomb3", here time, thetas, phis and sigs are vectors, which allows
!~      for non-uniform time bases, with different lengths etc.
      implicit none

      real*8, parameter  :: pi = 4*atan(1.)
      real*8, intent(in) :: time(:), thetas(:), phis(:), sigs(:), m, n, f

      real*8  :: P
      real*8  :: w, alpha, tau
      real*8  :: SSA, SCA, YY, YC, YS, CC, SS, alpha_coils(size(thetas))
      integer :: i, j, len_t, num_co

      len_t  = size(time)
      ! num_co = size(thetas)
      w      = 2*pi*f

!~ 		Calculate tau
      SSA = 0; SCA = 0
      do i=1, len_t
         alpha = 2*(-w*time(i) + m*thetas(i) + n*phis(i))
         SSA   = SSA + sin(alpha)
         SCA   = SCA + cos(alpha)
      end do
      tau = 0.5*atan(SSA/SCA)

      !~ 		Calculate periodogram
      YY = sum(sigs**2)
      YC=0.; YS=0.; CC=0.; SS=0.
      alpha_coils = m*thetas + n*phis - tau
      do i=1, len_t
         alpha = alpha_coils(i) - w*time(i)
         YC = YC + sigs(i)*cos(alpha)
         YS = YS + sigs(i)*sin(alpha)
         CC = CC + cos(alpha)**2
         SS = SS + sin(alpha)**2
      end do

      P = (1/YY) * ((YC**2)/CC + (YS**2)/SS)

   end function lomb3_difftimes

   function lomb3(time, thetas, phis, sigs, m, n, f) result(P)
!~ 		Calculates the Lomb periodogram with spatial dependencies given by the angles
!~      thetas and phis, for mode number m, n, and frequency f
      implicit none

      real*8, parameter  :: pi = 4*atan(1.)
      real*8, intent(in) :: time(:), thetas(:), phis(:), sigs(:,:), m, n, f

      real*8  :: P
      real*8  :: w, alpha, tau
      real*8  :: SSA, SCA, YY, YC, YS, CC, SS, alpha_tmp
      integer :: i, j, len_t, num_co

      len_t  = size(time)
      num_co = size(thetas)
      w      = 2*pi*f

!~ 		Calculate tau
      SSA = 0; SCA = 0
      do i=1, len_t, 1
         do j=1, num_co, 1
            alpha = 2*(-w*time(i) + m*thetas(j) + n*phis(j))
            SSA   = SSA + sin(alpha)
            SCA   = SCA + cos(alpha)
         end do
      end do
      tau = 0.5*atan(SSA/SCA)

!~ 		Calculate periodogram
      YY = sum(sigs**2)
      YC=0.; YS=0.; CC=0.; SS=0.
      do j=1, num_co
         alpha_tmp = m*thetas(j) + n*phis(j) - tau
         do i=1, len_t
            alpha = alpha_tmp - w*time(i)
            YC = YC + sigs(j, i)*cos(alpha)
            YS = YS + sigs(j, i)*sin(alpha)
            CC = CC + cos(alpha)**2
            SS = SS + sin(alpha)**2
         end do
      end do

      P = (1/YY) * ((YC**2)/CC + (YS**2)/SS)

   end function lomb3

   function lomb2(time, thetas, sigs, m, f) result(P)

      real*8, intent(in) :: time(:), thetas(:), sigs(:,:), m, f

      real*8, parameter :: pi=4.d0*atan(1.d0)
      real*8  :: P

      real*8  :: w, alpha, tau
      real*8  :: SSA, SCA, YY, YC, YS, CC, SS, alpha_tmp
      integer :: i, j, len_t, num_co

      len_t  = size(time)
      num_co = size(thetas)
      w      = 2*pi*f

!~ 		Calculate tau
      SSA = 0; SCA = 0
      do i=1, len_t, 1
         do j=1, num_co, 1
            alpha = 2*( -w*time(i) + m*thetas(j))
            SSA   = SSA + sin(alpha)
            SCA   = SCA + cos(alpha)
         end do
      end do
      tau = 0.5*atan(SSA/SCA)

!~ 		Calculate periodogram
      YY = sum(sigs**2)
      YC=0.; YS=0.; CC=0.; SS=0.
      do j=1, num_co
         alpha_tmp = m*thetas(j) - tau
         do i=1, len_t
            alpha = -w*time(i) + alpha_tmp
            YC = YC + sigs(j, i)*cos(alpha)
            YS = YS + sigs(j, i)*sin(alpha)
            CC = CC + cos(alpha)**2
            SS = SS + sin(alpha)**2
         end do
      end do

      P = (1/YY) * ((YC**2)/CC + (YS**2)/SS)

      return

   end function lomb2
end module helper

subroutine easylomb3_difftimes(time, thetas, phis, sigs, f, ns, ms, ntime, nn, nm, mapa)

   use helper, only : lomb3_difftimes

   integer, intent(in) :: ntime, nn, nm
   real*8, intent(in)  :: f, thetas(ntime), phis(ntime), ns(nn), ms(nm)
   real*8, intent(in)  :: time(ntime), sigs(ntime)

   real*8, intent(out) :: mapa(nn, nm)
   integer :: i, j
   real*8 :: tmp

!$OMP PARALLEL DO
   do j=1, nm
      do i=1, nn
         mapa(i,j) = lomb3_difftimes(time, thetas, phis, sigs, ms(j), ns(i), f)
      end do
   end do
!$OMP END PARALLEL DO

end subroutine easylomb3_difftimes

subroutine easylomb3(time, thetas, phis, sigs, f, ns, ms, ntime, ncoils, nn, nm, mapa)

   use helper, only : lomb3

   integer, intent(in) :: ntime, ncoils, nn, nm
   real*8, intent(in)  :: f, thetas(ncoils), phis(ncoils), ns(nn), ms(nm)
   real*8, intent(in)  :: time(ntime), sigs(ncoils, ntime)

   real*8, intent(out) :: mapa(nn, nm)
   integer :: i, j
   real*8 :: tmp

!$OMP PARALLEL DO
   do j=1, nm
      do i=1, nn
         mapa(i,j) = lomb3(time, thetas, phis, sigs, ms(j), ns(i), f)
      end do
   end do
!$OMP END PARALLEL DO

end subroutine easylomb3

subroutine easylomb2(time, thetas, sigs, f, ms, ntime, ncoils, nm, mapa)

   use helper, only : lomb2

   integer, intent(in) :: ntime, ncoils, nm
   real*8, intent(in)  :: f, thetas(ncoils), ms(nm)
   real*8, intent(in)  :: time(ntime), sigs(ncoils, ntime)

   real*8, intent(out) :: mapa(nm)
   integer             :: j
   real*8              :: tmp

!$OMP PARALLEL DO
   do j=1, nm
      mapa(j) = lomb2(time, thetas, sigs, ms(j), f)
   end do
!$OMP END PARALLEL DO

end subroutine easylomb2
