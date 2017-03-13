Contributing guide
##############################################################################

This page lists a set of guidelines for contributing to the project.
These are just guidelines, not rules, use your best judgment and feel
free to propose changes to this document in a pull request.

Reporting issues and making suggestions
==============================================================================

This section guides you through submitting an issue or making a suggestion
for the CS Unplugged project.
Following these guidelines helps maintainers and the community understand
your findings.

Before submitting an issue
------------------------------------------------------------------------------

- `Search the issue tracker for the issue/suggestion`_ to see if it has
  already been logged.
  If it has, add a comment to the existing issue (even if the issue is closed)
  instead of opening a new one.

How do I submit a (good) issue or suggestion?
------------------------------------------------------------------------------

Issues are tracked in the GitHub issue tracker (if you've never used
GitHub issues before, read this `10 minute guide to become a master`_).
When creating an issue, explain the problem and include additional details to
help maintainers understand or reproduce the problem:

For reporting an issue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Use a clear and descriptive title** for the issue to identify the problem.
- **Clearly and concisely describe the issue** and provide screenshots if
  required.
- **Link any related existing issues**.

If the issues is a code related issue, also include the following:

- **Describe the exact steps which reproduce the problem** in as many details
  as possible.
  For example, how you were generating a resource.
  When listing steps, **don't just say what you did, explain how you did it**.
- **Explain which behavior you expected to see instead and why.**
- **Describe the behavior you observed after following the steps** and point
  out what exactly is the problem with that behavior.
- **Can you reliably reproduce the issue?** If not, provide details about
  how often the problem happens and under which conditions it normally happens.
- **Include screenshots or animated GIFs** if it helps explain the issue you
  encountered.
- **What's the name and version of the OS you're using?**
- **What's the name and version of the browser you're using?**
- **If the problem is related to performance**, please provide
  specifications of your computer.

For making a suggestion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Explain the suggestion and include additional details to help maintainers
understand the changes:

- **Use a clear and descriptive title** for the issue to identify the
  suggestion.
- **Clearly and concisely describe the suggestion** and provide screenshots if
  required.
- **Explain why this suggestion would be useful** to most CS Unplugged users
  and isn't something that should be a implemented as a community variant of
  the project.
- **Link any related existing suggestions**.

Your first code contribution (pull request)
==============================================================================

Unsure where to begin contributing to CS Unplugged?
You can start by looking through the `issue tracker`_.

Pull requests
------------------------------------------------------------------------------

- **Include a detailed explaination** of the proposed change, including
  screenshots and animated GIFs in your pull request whenever possible.
- **Read and applied the style guides** listed below.
- Your pull request should be on a new branch from our ``develop`` branch,
  **that is being requested to merge back into** ``develop``.
  The naming conventions of branches should be descriptive of the new
  addition/modification.
  Ideally they would specify their namespace as well, for example:

  - ``resource/puzzle-town``
  - ``topic/algorithms``
  - ``issue/234``

- Link to any relevant existing issues/suggestions.
- Added necessary documentation (if appropriate).

We aim to keep the CS Unplugged project as robust as possible, so please do
your best to ensure your changes won't break anything!

Style guides
==============================================================================

Git
------------------------------------------------------------------------------

- Commits should be as descriptive as possible.
  Other developers (and even future you) will thank you for your forethought
  and verbosity for well documented commits.
  Generally:

  - Limit the first line to 72 characters or less
  - Reference issues and pull requests liberally

- We use `Vincent Driessen's Git Branching Model <http://nvie.com/posts/a-successful-git-branching-model/>`_
  for managing development.
  Please read this document to understand our branching methods.

Project structure
------------------------------------------------------------------------------

- Folders should be all lowercase with dashes for spaces.
- Folders and files should use full words when named, however JavaScript, CSS,
  and image folders can be named ``js``, ``css``, and ``img`` respectively.

Text (Markdown)
------------------------------------------------------------------------------

- Each sentence should be started on a newline (this greatly improves
  readability when comparing two states of a document).

Programming
------------------------------------------------------------------------------

Quote from Google style guides:

  Be consistent.

  If you’re editing code, take a few minutes to look at the code around you
  and determine its style.
  If they use spaces around all their arithmetic operators, you should too.
  If their comments have little boxes of hash marks around them, make your
  comments have little boxes of hash marks around them too.

  The point of having style guidelines is to have a common vocabulary of coding
  so people can concentrate on what you’re saying rather than on how you’re
  saying it.
  We present global style rules here so people know the vocabulary, but local
  style is also important.
  If code you add to a file looks drastically different from the existing code
  around it, it throws readers out of their rhythm when they go to read it.
  Avoid this.

We aim to abide by the following style guides:

- **Python** - We follow `PEP8`_ except for one change of line length.
  `Django recommends allowing 119 characters`_, so we use this as our line
  length limit.
- **HTML** - We follow the `open source HTML style guide`_ by @mdo.
- **CSS** - We follow the `open source CSS style guide`_ by @mdo.
- **JavaScript** - We follow the `Google JavaScript style guide`_.

.. _Search the issue tracker for the issue/suggestion: https://github.com/uccser/cs-unplugged/issues?utf8=%E2%9C%93&q=is%3Aissue
.. _10 minute guide to become a master: https://guides.github.com/features/issues/
.. _issue tracker: https://github.com/uccser/cs-unplugged/issues
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _Django recommends allowing 119 characters: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
.. _open source HTML style guide: http://codeguide.co/#html
.. _open source CSS style guide: http://codeguide.co/#css
.. _Google JavaScript style guide: https://google.github.io/styleguide/javascriptguide.xml
