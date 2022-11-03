pulls_walk_alpha = load(['./Data/Model/pullsWalk/alpha.mat']).alpha;
pulls_stand_alpha = load(['./Data/Model/pullsStand/alpha.mat']).alpha;
walk_rotate_alpha = load(['./Data/Model/walkRotate/alpha.mat']).alpha;
stand_rotate_alpha = load(['./Data/Model/standRotate/alpha.mat']).alpha;
pulls_walk_theta = load(['./Data/Model/pullsWalk/theta.mat']).theta;
pulls_stand_theta = load(['./Data/Model/pullsStand/theta.mat']).theta;
walk_rotate_theta = load(['./Data/Model/walkRotate/theta.mat']).theta;
stand_rotate_theta = load(['./Data/Model/standRotate/theta.mat']).theta;
pulls_walk_all = load(['./Data/Model/pullsWalk/all.mat']).all;
pulls_stand_all = load(['./Data/Model/pullsStand/all.mat']).all;
walk_rotate_all = load(['./Data/Model/walkRotate/all.mat']).all;
stand_rotate_all = load(['./Data/Model/standRotate/all.mat']).all;

%tests
%------------------b------------------------
% differenece in standing and wlaking in different bands
x1a = pulls_walk_alpha(1:8,1:8);
y1a = pulls_stand_alpha(1:8,1:8);
x2a = walk_rotate_alpha(1:8,1:8);
y2a = stand_rotate_alpha(1:8,1:8);

x1t = pulls_walk_theta(1:8,1:8);
y1t = pulls_stand_theta(1:8,1:8);
x2t = walk_rotate_theta(1:8,1:8);
y2t = stand_rotate_theta(1:8,1:8);

x1l = pulls_walk_all(1:8,1:8);
y1l = pulls_stand_all(1:8,1:8);
x2l = walk_rotate_all(1:8,1:8);
y2l = stand_rotate_all(1:8,1:8);
%task comparison
disp('---------------------cortico-cortical connectivity---------------------------');
fprintf('\n');
disp('walk vs stand');
[h,p] = ttest([x1a(:);x2a(:)],[y1a(:);y2a(:)]);
disp(['     alpha band - pvalue:' num2str(p)]);

[h,p] = ttest([x1t(:);x2t(:)],[y1t(:);y2t(:)]);
disp(['     theta band - pvalue:' num2str(p)]);

[h,p] = ttest([x1l(:);x2l(:)],[y1l(:);y2l(:)]);
disp(['     all band - pvalue:' num2str(p)]);
fprintf('\n');
%perturbation
disp('pull vs rotation');
[h,p] = ttest([x1a(:);y1a(:)],[x2a(:);y2a(:)]);
disp(['     alpha band - pvalue:' num2str(p)]);

[h,p] = ttest([x1t(:);y1t(:)],[x2t(:);y2t(:)]);
disp(['     theta band - pvalue:' num2str(p)]);

[h,p] = ttest([x1l(:);y1l(:)],[x2l(:);y2l(:)]);
disp(['     all band - pvalue:' num2str(p)]);
fprintf('\n');
%------------------b------------------------
x1a = pulls_stand_alpha(9:12,9:12);
x2a = pulls_walk_alpha(9:12,9:12);
x3a = pulls_stand_alpha(9:12,13:16);
x4a = pulls_walk_alpha(9:12,13:16);

x1t = pulls_stand_theta(9:12,9:12);
x2t = pulls_walk_theta(9:12,9:12);
x3t = pulls_stand_theta(9:12,13:16);
x4t = pulls_walk_theta(9:12,13:16);

x1l = pulls_stand_all(9:12,9:12);
x2l = pulls_walk_all(9:12,9:12);
x3l = pulls_stand_all(9:12,13:16);
x4l = pulls_walk_all(9:12,13:16);
disp('---------------------muscular connectivity-----------------------------------');
fprintf('\n');
%intra vs inter
fprintf('intra-leg vs inter-leg\n');
[h,p] = ttest([x1a(:);x2a(:)],[x3a(:);x4a(:)]);
disp(['     alpha band - pvalue:' num2str(p)]);

[h,p] = ttest([x1t(:);x2t(:)],[x3t(:);x4t(:)]);
disp(['     theta band - pvalue:' num2str(p)]);

[h,p] = ttest([x1l(:);x2l(:)],[x3l(:);x4l(:)]);
disp(['     all band - pvalue:' num2str(p)]);
fprintf('\n');
%intra-leg stand and walk
fprintf('intra-leg stand and walk\n');
[h,p] = ttest(x1a(:),x2a(:));
disp(['     alpha band - pvalue:' num2str(p)]);

[h,p] = ttest(x1t(:),x2t(:));
disp(['     theta band - pvalue:' num2str(p)]);

[h,p] = ttest(x1l(:),x2l(:));
disp(['     all band - pvalue:' num2str(p)]);
fprintf('\n')
%inter-leg stand and walk
fprintf('inter-leg stand and walk\n');
[h,p] = ttest(x3a(:),x4a(:));
disp(['     alpha band - pvalue:' num2str(p)]);

[h,p] = ttest(x3t(:),x4t(:));
disp(['     theta band - pvalue:' num2str(p)]);

[h,p] = ttest(x3l(:),x4l(:));
disp(['     all band - pvalue:' num2str(p)]);
fprintf('\n')
%------------------c------------------------
x1a = pulls_stand_alpha(9:16,1:8);
x2a = pulls_walk_alpha(9:16,1:8);
x3a = pulls_stand_alpha(1:8,9:16);
x4a = pulls_walk_alpha(1:8,9:16);

x1t = pulls_stand_theta(9:16,1:8);
x2t = pulls_walk_theta(9:16,1:8);
x3t = pulls_stand_theta(1:8,9:16);
x4t = pulls_walk_theta(1:8,9:16);

x1l = pulls_stand_all(9:16,1:8);
x2l = pulls_walk_all(9:16,1:8);
x3l = pulls_stand_all(1:8,9:16);
x4l = pulls_walk_all(1:8,9:16);

disp('-----------------------corticomuscular connectivity----------------------------');
fprintf('\n');
%corticomuscular stand and walk
fprintf('corticomuscular stand and walk\n');
[h,p] = ttest([x1a(:);x3a(:)],[x2a(:);x4a(:)]);
disp(['     alpha band - pvalue:' num2str(p)]);

[h,p] = ttest([x1t(:);x3t(:)],[x2t(:);x4t(:)]);
disp(['     theta band - pvalue:' num2str(p)]);

[h,p] = ttest([x1l(:);x3l(:)],[x2l(:);x4l(:)]);
disp(['     all band - pvalue:' num2str(p)]);
fprintf('\n')
%cortex to muscles vs muscles to cortex
fprintf('cortex to muscles vs muscles to cortex\n');
[h,p] = ttest([x1a(:);x2a(:)],[x3a(:);x4a(:)]);
disp(['     alpha band - pvalue:' num2str(p)]);

[h,p] = ttest([x1t(:);x2t(:)],[x3t(:);x4t(:)]);
disp(['     theta band - pvalue:' num2str(p)]);

[h,p] = ttest([x1l(:);x2l(:)],[x3l(:);x4l(:)]);
disp(['     all band - pvalue:' num2str(p)]);
fprintf('\n')


