%% setup
N = 20 %number of samples to compute
imp = zeros(N,1); %creates a list of zeros, length N
imp(3) = 1; % sets the third sample to one. So we have an impulse.

%% processing
x0 = [imp;0]; %takes the input and append a zero.
x1 = [0;imp]; %takes the input and prepends a zero(= delay input 1 sample).
Y = x0+x1; %computes the output signal.

%% Plotting
% plot input
subplot(2,1,1)
stem(x0)
xlabel('n')
ylim([-0.1, 1.1])
grid on
xlim([0,N+2])
title('Input Signal')
% plot output
subplot(2,1,2)
stem(Y)
xlabel('n')
ylim([-0.1, 1.1])
xlim([0,N+2])
grid on
title('Output Signal')