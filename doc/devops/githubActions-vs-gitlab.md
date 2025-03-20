
# github actions vs gitlab

It is possible to use GitHub Actions with GitLab, however there are some considerations and limitations to keep in mind.

## Implementation Considerations

- When adapting GitHub Actions for GitLab, you'll need to modify the configuration syntax. GitLab uses `.gitlab-ci.yml` instead of the `.github/workflows` directory used by GitHub.

- You may need to translate certain GitHub-specific constructs to their GitLab equivalents. For example, `uses` in GitHub Actions corresponds to `include` in GitLab CI/CD.

- Some manual adjustments may be required, such as handling masked variables and artifact reports.

## References:
- https://graphite.dev/guides/gitlab-cicd--vs-github-actions
- https://blog.realkinetic.com/gitlab-ci-cd-vs-github-actions-a-comprehensive-comparison-f304422124db 



