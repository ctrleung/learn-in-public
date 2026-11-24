# Topics I should know

The source of truth for the mastery map: one section per subject, one row per topic, each with an "I can..." line that makes it testable. Topics with no review items yet show as grey ("not started"). This is a draft, polished one subject at a time.

How to read the tags: **[plan]** is already in `PLAN.md`; **[added?]** is a suggestion, to keep or cut.

## HTML (draft 1, to edit)

| # | Topic | I can... | Tag |
|---|---|---|---|
| 1 | Element anatomy and attributes | name the parts of an element, tell an element from a tag, say what a void element is, write attributes, nest elements correctly, add comments and say that tag and attribute names are case-insensitive | plan |
| 2 | Document structure | say what the doctype does, write the skeleton (`html` with `lang`, `head`, `body`) and say which parts are required | plan |
| 3 | Metadata | set the title, charset, viewport and description, and link a stylesheet, script and icon | plan |
| 4 | Headings and paragraphs | pick heading levels for structure, not size, avoid skipped levels, and explain whitespace collapsing, `br` and `hr` | plan |
| 5 | Text semantics | choose `em`, `strong`, `code`, `pre`, `abbr`, `time`, `blockquote`, `cite`, `q`, `dfn`, `address`, `mark`, `sub`, `sup`, `del`, `ins` and `s` for their meaning, and say why `b` and `i` are different | plan |
| 6 | Lists | pick `ul`, `ol` or `dl`, nest lists, and say why a menu of links is a list | plan |
| 7 | Links | write absolute and relative URLs, anchors and fragments, write link text that makes sense alone, and use `mailto`, `download` and `rel` | plan |
| 8 | Images and media | write useful `alt` text (and empty `alt` for decoration), use `figure` and `figcaption`, set width and height, and know what `picture`, `srcset`, `loading` and `fetchpriority` do | plan |
| 9 | Page structure and landmarks | use `header`, `nav`, `main`, `article`, `section`, `aside` and `footer`, and say when `div` and `span` are the right choice | plan |
| 10 | Forms | build a form with `label`, `input` types, `select`, `textarea`, `button` and `fieldset`, and say how `name`, GET and POST decide what is sent | plan |
| 11 | Form validation | use `required`, `type`, `pattern`, `min` and `max`, explain why client-side validation is not enough, and say what the server must still check | plan |
| 12 | Tables | build an accessible data table with `caption`, `thead`, `tbody`, `th scope`, `colspan` and `rowspan`, and say when not to use a table | plan |
| 13 | Accessibility basics | say what accessibility is, who it helps, and what an accessible name and the accessibility tree are | plan |
| 14 | Keyboard and focus | use a page with only the keyboard, explain tab order and `tabindex`, and keep visible focus and a skip link | plan |
| 15 | WAI-ARIA basics | use `role`, `aria-label` and `aria-labelledby`, and state the first rule of ARIA (use native HTML first) | plan |
| 16 | Accessibility tooling | run an automated checker, read the accessibility tree in DevTools and try a screen reader | plan |
| 17 | Character references and entities | write `&amp;`, `&lt;`, `&nbsp;` and say why you escape `<` in text | added? |
| 18 | Embedded content | use `iframe` safely (`title`, `sandbox`) and know what `video` and `audio` need | added? |
| 19 | Interactive elements | use `details` and `summary`, and say what the `dialog` element gives you | added? |
| 20 | HTML and security | say how unescaped input becomes XSS, why `rel="noopener"` exists, what a content security policy (CSP) is for, and what `iframe sandbox` does | added? |
| 21 | Validity and parsing | run a validator, say how the browser recovers from broken HTML, and tell semantic from presentational markup | added? |
| 22 | Global attributes | use `id` and `class` well, store data in `data-*` attributes, say why `style` in HTML is a last resort, and use `hidden`, `lang` and `title` | added? |
| 23 | SEO basics | write a useful `title` and meta description, use headings and link text that make sense out of context, and say what is page-level and what is not | added? |

## CSS (draft 2, to edit)

| # | Topic | I can... | Tag |
|---|---|---|---|
| 1 | CSS syntax and how it is applied | write a rule (selector, property, value, declaration block), add CSS with `link`, `style` and inline `style`, write comments, and say which to use when | plan |
| 2 | Selectors | use type, class, ID, attribute and universal selectors, group selectors, and say which selector to reach for first | plan |
| 3 | Combinators, pseudo-classes and pseudo-elements | use descendant, child and sibling combinators, `:hover`, `:focus-visible`, `:nth-child` and `::before`, and say what each matches | plan |
| 4 | The cascade | say how the origin, cascade layers (`@layer`), specificity and source order decide which rule wins, and where `!important` fits | plan |
| 5 | Specificity | work out which of two selectors is more specific, and keep specificity low and predictable | plan |
| 6 | Inheritance and resetting | say which properties inherit, and use `inherit`, `initial`, `unset` and `revert` | plan |
| 7 | The box model | name content, padding, border and margin, use `box-sizing: border-box`, explain margin collapsing, and use `outline` and `box-shadow` | plan |
| 8 | Sizing and overflow | use `width`, `height`, `min-` and `max-` sizes, percentages and content-based sizes, and control `overflow` | plan |
| 9 | Values, units and functions | choose between `px`, `rem`, `em`, `%`, `vw` and `vh`, and use `calc()`, `min()`, `max()`, `clamp()`, `var()`, `url()`, `attr()` and `color-mix()` | plan |
| 10 | Colors and backgrounds | write colors in hex, `rgb()`, `hsl()` and modern formats, set `opacity`, set backgrounds (color, image, gradient, size, position, repeat, attachment), and check text contrast | plan |
| 11 | Typography and text styling | set `font-family` stacks, size, weight, style, shorthand and `line-height`, load a web font, align, decorate, transform and space text, use `text-shadow`, set text direction, and keep a readable line length | plan |
| 12 | Display and normal flow | explain block and inline flow, `display` values, and how `inline-block` and `none` differ from `visibility: hidden` | plan |
| 13 | Positioning | use `relative`, `absolute`, `fixed` and `sticky`, say what each is positioned against, and explain `z-index` and stacking contexts | plan |
| 14 | Flexbox | lay out a row or a column, align and distribute items, and use `gap`, `flex-grow`, `flex-shrink` and `flex-basis` | plan |
| 15 | Grid | define columns and rows, place items, use `fr`, `repeat()` and `minmax()`, and choose between grid and flexbox | plan |
| 16 | Floats and multi-column layout | say what `float` and `clear` were for, recognise them in old code, and use `columns` for text | added? |
| 17 | Responsive design | set the viewport meta, write mobile-first media queries, use fluid layouts and relative units, size images responsively, and scale text fluidly with `clamp()` | plan |
| 18 | Container queries | size a component by its container with `@container`, and say when to prefer it over a media query | added? |
| 19 | Styling links and lists | style link states in the right order, lists and their markers, and keep focus visible | plan |
| 20 | Styling forms and tables | style inputs, buttons and tables, and say why form controls need special care | plan |
| 21 | Images, filters and replaced elements | use `object-fit`, `aspect-ratio` and `max-width: 100%`, apply `filter` and blend modes, and say what makes an element "replaced" | added? |
| 22 | Custom properties and theming | define and use `--` variables, scope them, and build light and dark themes with `prefers-color-scheme` | added? |
| 23 | CSS and accessibility | keep focus styles and contrast, respect `prefers-reduced-motion`, hide content visually without hiding it from screen readers, and avoid relying on color alone | plan |
| 24 | Transitions and animations | write a transition and a `@keyframes` animation, say which properties animate cheaply, and respect reduced motion | added? |
| 25 | Transforms | use `translate`, `scale`, `rotate` and `transform-origin`, and say why transforms do not affect layout | added? |
| 26 | Modern selectors and nesting | use `:is()`, `:where()` and `:has()`, and write nested rules | added? |
| 27 | Logical properties and `@supports` | use logical properties such as `margin-inline` for different writing directions, and test for a feature with `@supports` | added? |
| 28 | Debugging CSS with DevTools | inspect an element, read the computed styles and the box model, find the winning rule, and toggle declarations | plan |
| 29 | Organizing CSS | name classes consistently, order a stylesheet, use a reset, and say what BEM or utility-first CSS trade off | added? |
| 30 | How CSS is loaded and rendered | say why CSS blocks rendering, what a render-blocking stylesheet costs, and how to keep it small | added? |

Parked, not in the list: Sass and PostCSS (not needed for the fundamentals), and CSS Modules and CSS-in-JS (they fit better with React).

## JavaScript (draft 2, to edit)

Level is from your JavaScript roadmap: green is beginner, purple is intermediate, black is advanced. Topics not on that roadmap have no level. Level is a hint for choosing what to teach next, not something shown on the map: within a block go beginner, then intermediate, then advanced; open gaps and due reviews come first; an advanced topic waits until the topics it builds on have passed their first re-test. Tag: `plan` is in `PLAN.md`, `roadmap` is from your roadmap, `added?` is my suggestion.

| # | Topic | I can... | Level | Tag |
|---|---|---|---|---|
| 1 | What JavaScript is and how it runs | say what JavaScript and ECMAScript are, run code in the browser console, a script tag and Node, and say what strict mode changes | beginner | roadmap |
| 2 | Variables and data types | use `let` and `const` (and say why not `var`), follow naming rules, explain hoisting once, name the primitive types including `bigint` and `symbol`, use `typeof`, tell `null` from `undefined`, explain type coercion and explicit conversion, and choose `===` over `==` and know `Object.is` | beginner | plan |
| 3 | Operators and control flow | write `if`, `switch` and ternaries, say what is truthy and falsy, use `&&`, `||`, `??` and `?.`, and write `for`, `while`, `do...while`, `for...of` and `for...in` loops with `break` and `continue` | beginner | plan |
| 4 | Functions | write declarations, expressions and arrow functions, use default and rest parameters and the `arguments` object, write an IIFE and a recursive function, and use built-in functions | beginner | plan |
| 5 | Scope and closures | say what block, function and global scope and lexical scoping are, and explain a closure with an example you could use in real code | intermediate | plan |
| 6 | `this` and binding | say what `this` is in a method, a function, an event handler and an arrow function, and use `call`, `apply` and `bind` | intermediate | plan |
| 7 | Objects and prototypes | create objects, read and change properties, use destructuring and spread, use `Object.keys` and `Object.entries`, and explain the prototype chain and prototypal inheritance | intermediate | plan |
| 8 | Classes | write a class with `constructor`, methods, `extends`, getters and private fields, and say how classes relate to prototypes | intermediate | roadmap |
| 9 | Arrays and iteration | use `map`, `filter`, `reduce`, `find`, `some`, `every` and `for...of`, sort correctly, and say which methods change the array | beginner | plan |
| 10 | Strings, numbers, dates and math | use template literals and string methods, explain floating-point surprises, work with `Date` and `Intl`, and use `Math` | beginner | plan |
| 11 | Collections | use `Map`, `Set`, `WeakMap` and `WeakSet`, say what a typed array is, and say when each beats an object or an array | intermediate | roadmap |
| 12 | Iterators and generators | say what the iterator protocol is, write a generator with `yield`, and say when you would use one | advanced | roadmap |
| 13 | Modules and loading scripts | use `import` and `export`, load a script with `type="module"`, explain `defer` and `async`, and recognise CommonJS in Node code | intermediate | plan |
| 14 | The DOM: selecting and changing | use `querySelector`, `textContent`, `createElement`, `classList` and attributes, and say why `textContent` is safer than `innerHTML` | intermediate | plan |
| 15 | Events | add and remove listeners, read the event object, and tell `target` from `currentTarget` | intermediate | plan |
| 16 | Event bubbling, capturing and delegation | explain the three phases, stop propagation, and use event delegation on a list | intermediate | plan |
| 17 | The event loop and timers | explain the call stack, the task queue and microtasks, use `setTimeout` and `setInterval`, and predict the order of timer and promise callbacks | advanced | plan |
| 18 | Callbacks and promises | say what callback hell is, say what the three promise states are, chain `then`, `catch` and `finally`, and use `Promise.all`, `race` and `allSettled` | intermediate | plan |
| 19 | async and await | write `async` functions, handle errors with `try` and `catch`, and run requests in sequence and in parallel | intermediate | plan |
| 20 | fetch and HTTP in the browser | use `fetch` with methods, headers and a body, check `response.ok`, cancel with `AbortController`, say why a 404 does not reject, and recognise `XMLHttpRequest` in old code | beginner | plan |
| 21 | JSON | use `JSON.parse` and `JSON.stringify`, say what JSON cannot hold, and handle bad JSON | beginner | plan |
| 22 | Error handling | use `try`, `catch`, `finally` and `throw`, know the built-in error types, write a custom error, and show an error to the user | beginner | plan |
| 23 | Browser storage | use `localStorage`, `sessionStorage` and cookies, say how they differ, and say what must never be stored there | — | plan |
| 24 | Forms and user input | read a form with `FormData`, handle `submit` with `preventDefault`, and use the constraint validation API | — | added? |
| 25 | Browser APIs | use `URL` and `URLSearchParams`, `history`, `IntersectionObserver`, timers and `requestAnimationFrame` | — | added? |
| 26 | Security basics in JavaScript | say how `innerHTML` and `eval` lead to XSS, what CORS blocks from `fetch`, what a CSP does, and why not to keep secrets in front-end code | — | plan |
| 27 | Debugging and DevTools | use the console, breakpoints, the network tab and stack traces to find a bug, and use DevTools to find a memory leak or a slow function | intermediate | plan |
| 28 | Memory management | describe the memory lifecycle, say how garbage collection decides what to free, and name common causes of memory leaks | advanced | roadmap |
| 29 | Performance and the main thread | say what blocks the main thread, use debouncing and throttling, and know when a worker helps | — | added? |
| 30 | Tooling and packages | use `npm` and `package.json`, and say what a bundler, linter and formatter do | — | added? |
| 31 | Testing basics | write a small unit test with an assertion, and say what makes a function easy to test | — | added? |
| 32 | Regular expressions | read and write simple patterns, and use `match`, `test` and `replace` | — | added? |

Parked, not in the list: TypeScript, Node.js and back-end JavaScript, frameworks other than React, and the bitwise, comma and BigInt operators.

## React, Networking and HTTP

To be drafted, one subject at a time. The first guesses are in the script (`scripts/mastery_map.py`) and the plan (`PLAN.md`, weeks 10 to 12).
