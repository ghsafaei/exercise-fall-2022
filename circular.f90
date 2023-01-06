program main_my
 implicit none
 real G,M,r,v
 G=0.0043!4.3*10.0**-3
 M=10.0**11.
 r=8500.
 v=sqrt(G*m/r)
  print*,'r=8.5 kpc','------','v=',v
!!!!!!!!!!!!!!!!!!!!!!
 r=8000.
 v=sqrt(G*m/r)
  print*,'r=8.0 kpc','------','v=',v
!!!!!!!!!!!!!!!!!!!!!!
 r=5000.
 v=sqrt(G*m/r)
  print*,'r=5.0 kpc','------','v=',v
!!!!!!!!!!!!!!!!!!!!!!
 r=3000.
 v=sqrt(G*m/r)
  print*,'r=3.0 kpc','------','v=',v
!!!!!!!!!!!!!!!!!!!!!!
 r=10000.
 v=sqrt(G*m/r)
  print*,'r=10.0 kpc','------','v=',v
end
