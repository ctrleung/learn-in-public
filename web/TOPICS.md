# Topics I should know

The source of truth for the mastery map: one section per subject, one row per topic, each with an "I can..." line that makes it testable. Topics with no review items yet show as grey ("not started"). All subjects are drafted; edit anything.

Tag: `plan` means the topic is in `PLAN.md`; `extra` means it is on top of the plan (from your roadmaps or my suggestions), and you can cut any of them.

## HTML

| # | Topic | I can... | Tag |
|---|---|---|---|
| 1 | Element anatomy and attributes | name the parts of an element (the element, opening tag, content, closing tag and attributes) and tell an element from a tag, say what a void element is and how it differs from other elements, write attributes, explain why HTML must be correctly nested, add comments, and say that tag and attribute names are case-insensitive | plan |
| 2 | Document structure | say why a page needs a doctype, what it was originally for (standards mode vs quirks mode) and why it is now somewhat of a historical artifact, and write the skeleton (`html` with `lang`, `head`, and `body` as the container for the page content), saying which parts are required | plan |
| 3 | Metadata | set the title, charset, viewport and description, and link a stylesheet, script and icon | plan |
| 4 | Headings and paragraphs | pick heading levels for structure, not size, avoid skipped levels, and explain whitespace collapsing, `br` and `hr` | plan |
| 5 | Emphasis and code | choose `em`, `strong`, `code`, `pre`, `mark`, `sub`, `sup` and `time` for their meaning, and say why `b` and `i` are different | plan |
| 6 | Quotes, edits and annotations | use `blockquote`, `q`, `cite`, `abbr`, `dfn`, `address`, `del`, `ins` and `s`, and say what each means | plan |
| 7 | Lists | pick `ul`, `ol` or `dl`, nest lists, and say why a menu of links is a list | plan |
| 8 | Links | write absolute and relative URLs, anchors and fragments, write link text that makes sense alone, and use `mailto`, `download` and `rel` | plan |
| 9 | Images and media | write useful `alt` text (and empty `alt` for decoration), use `figure` and `figcaption`, set width and height, and know what `picture`, `srcset`, `loading` and `fetchpriority` do | plan |
| 10 | Page structure and landmarks | use `header`, `nav`, `main`, `article`, `section`, `aside` and `footer`, and say when `div` and `span` are the right choice | plan |
| 11 | Forms | build a form with `label`, `input` types, `select`, `textarea`, `button` and `fieldset`, and say how `name`, GET and POST decide what is sent | plan |
| 12 | Form validation | use `required`, `type`, `pattern`, `min` and `max`, explain why client-side validation is not enough, and say what the server must still check | plan |
| 13 | Tables | build an accessible data table with `caption`, `thead`, `tbody`, `th scope`, `colspan` and `rowspan`, and say when not to use a table | plan |
| 14 | Accessibility basics | say what accessibility is, who it helps, and what an accessible name and the accessibility tree are | plan |
| 15 | Keyboard and focus | use a page with only the keyboard, explain tab order and `tabindex`, and keep visible focus and a skip link | plan |
| 16 | WAI-ARIA basics | use `role`, `aria-label` and `aria-labelledby`, and state the first rule of ARIA (use native HTML first) | plan |
| 17 | Accessibility tooling | run an automated checker, read the accessibility tree in DevTools and try a screen reader | plan |
| 18 | Character references and entities | write `&amp;`, `&lt;`, `&nbsp;` and say why you escape `<` in text | extra |
| 19 | Embedded content | use `iframe` safely (`title`, `sandbox`) and know what `video` and `audio` need | extra |
| 20 | Interactive elements | use `details` and `summary`, and say what the `dialog` element gives you | extra |
| 21 | HTML and security | say how unescaped input becomes XSS, why `rel="noopener"` exists, and what `iframe sandbox` does | extra |
| 22 | Validity and parsing | run a validator, say how the browser recovers from broken HTML, and tell semantic from presentational markup | extra |
| 23 | Global attributes | use `id` and `class` well, store data in `data-*` attributes, say why `style` in HTML is a last resort, and use `hidden`, `lang` and `title` | extra |
| 24 | SEO basics | write a useful `title` and meta description, use headings and link text that make sense out of context, and say what is page-level and what is not | extra |
| 25 | Progressive enhancement and browser support | say what progressive enhancement is, check browser support, use feature detection and sensible fallbacks, and build a page that still works without JavaScript or modern CSS | extra |

## CSS

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
| 9 | Values and units | choose between `px`, `rem`, `em`, `%`, `vw` and `vh`, and say how relative units compound | plan |
| 10 | CSS functions | use `calc()`, `min()`, `max()`, `clamp()`, `var()`, `url()`, `attr()` and `color-mix()` | plan |
| 11 | Colors and backgrounds | write colors in hex, `rgb()`, `hsl()` and modern formats, set `opacity`, set backgrounds (color, image, gradient, size, position, repeat, attachment), and check text contrast | plan |
| 12 | Fonts and web fonts | set `font-family` stacks, size, weight, style and the `font` shorthand, load a web font, and say what a fallback stack is for | plan |
| 13 | Text styling | set `line-height`, align, decorate, transform and space text, use `text-shadow`, set text direction, and keep a readable line length | plan |
| 14 | Display and normal flow | explain block and inline flow, `display` values, and how `inline-block` and `none` differ from `visibility: hidden` | plan |
| 15 | Positioning | use `relative`, `absolute`, `fixed` and `sticky`, say what each is positioned against, and explain `z-index` and stacking contexts | plan |
| 16 | Flexbox | lay out a row or a column, align and distribute items, and use `gap`, `flex-grow`, `flex-shrink` and `flex-basis` | plan |
| 17 | Grid | define columns and rows, place items, use `fr`, `repeat()` and `minmax()`, and choose between grid and flexbox | plan |
| 18 | Floats and multi-column layout | say what `float` and `clear` were for, recognise them in old code, and use `columns` for text | extra |
| 19 | Responsive design | set the viewport meta, write mobile-first media queries, use fluid layouts and relative units, size images responsively, and scale text fluidly with `clamp()` | plan |
| 20 | Container queries | size a component by its container with `@container`, and say when to prefer it over a media query | extra |
| 21 | Styling links and lists | style link states in the right order, lists and their markers, and keep focus visible | plan |
| 22 | Styling forms and tables | style inputs, buttons and tables, and say why form controls need special care | plan |
| 23 | Images, filters and replaced elements | use `object-fit`, `aspect-ratio` and `max-width: 100%`, apply `filter` and blend modes, and say what makes an element "replaced" | extra |
| 24 | Custom properties and theming | define and use `--` variables, scope them, and build light and dark themes with `prefers-color-scheme` | extra |
| 25 | CSS and accessibility | keep focus styles and contrast, respect `prefers-reduced-motion`, hide content visually without hiding it from screen readers, and avoid relying on color alone | plan |
| 26 | Transitions and animations | write a transition and a `@keyframes` animation, say which properties animate cheaply, and respect reduced motion | extra |
| 27 | Transforms | use `translate`, `scale`, `rotate` and `transform-origin`, and say why transforms do not affect layout | extra |
| 28 | Modern selectors and nesting | use `:is()`, `:where()` and `:has()`, and write nested rules | extra |
| 29 | Logical properties and `@supports` | use logical properties such as `margin-inline` for different writing directions, and test for a feature with `@supports` | extra |
| 30 | Debugging CSS with DevTools | inspect an element, read the computed styles and the box model, find the winning rule, and toggle declarations | plan |
| 31 | Organizing CSS | name classes consistently, order a stylesheet, use a reset, and say what BEM or utility-first CSS trade off | extra |
| 32 | How CSS is loaded and rendered | say why CSS blocks rendering, what a render-blocking stylesheet costs, and how to keep it small | extra |

Parked, not in the list: Sass and PostCSS (not needed for the fundamentals), and CSS Modules and CSS-in-JS (they fit better with React).

## JavaScript

Level (from your JavaScript roadmap) helps me pick what to teach next: beginner first, then intermediate, then advanced. Open gaps and due reviews come first, and an advanced topic waits until the topics it builds on have passed their first re-test. It is not shown on the map.

| # | Topic | I can... | Level | Tag |
|---|---|---|---|---|
| 1 | What JavaScript is and how it runs | say what JavaScript and ECMAScript are, run code in the browser console, a script tag and Node, and say what strict mode changes | beginner | extra |
| 2 | Variables and hoisting | use `let` and `const` (and say why not `var`), follow naming rules, and explain hoisting | beginner | plan |
| 3 | Data types, coercion and equality | name the primitive types including `bigint` and `symbol`, use `typeof`, tell `null` from `undefined`, explain type coercion and explicit conversion, and choose `===` over `==` and know `Object.is` | beginner | plan |
| 4 | Operators and control flow | write `if`, `switch` and ternaries, say what is truthy and falsy, use `&&`, the logical or operator, `??` and `?.`, and write `for`, `while`, `do...while`, `for...of` and `for...in` loops with `break` and `continue` | beginner | plan |
| 5 | Functions | write declarations, expressions and arrow functions, use default and rest parameters and the `arguments` object, write an IIFE and a recursive function, and use built-in functions | beginner | plan |
| 6 | Scope and closures | say what block, function and global scope and lexical scoping are, and explain a closure with an example you could use in real code | intermediate | plan |
| 7 | `this` and binding | say what `this` is in a method, a function, an event handler and an arrow function, and use `call`, `apply` and `bind` | intermediate | plan |
| 8 | Objects and prototypes | create objects, read and change properties, use destructuring and spread, use `Object.keys` and `Object.entries`, and explain the prototype chain and prototypal inheritance | intermediate | plan |
| 9 | Classes | write a class with `constructor`, methods, `extends`, getters and private fields, and say how classes relate to prototypes | intermediate | extra |
| 10 | Arrays and iteration | use `map`, `filter`, `reduce`, `find`, `some`, `every` and `for...of`, sort correctly, and say which methods change the array | beginner | plan |
| 11 | Strings, numbers, dates and math | use template literals and string methods, explain floating-point surprises, work with `Date` and `Intl`, and use `Math` | beginner | plan |
| 12 | Collections | use `Map`, `Set`, `WeakMap` and `WeakSet`, say what a typed array is, and say when each beats an object or an array | intermediate | extra |
| 13 | Iterators and generators | say what the iterator protocol is, write a generator with `yield`, and say when you would use one | advanced | extra |
| 14 | Modules and loading scripts | use `import` and `export`, load a script with `type="module"`, explain `defer` and `async`, and recognise CommonJS in Node code | intermediate | plan |
| 15 | The DOM: selecting and changing | use `querySelector`, `textContent`, `createElement`, `classList` and attributes, and say why `textContent` is safer than `innerHTML` | intermediate | plan |
| 16 | Events | add and remove listeners, read the event object, and tell `target` from `currentTarget` | intermediate | plan |
| 17 | Event bubbling, capturing and delegation | explain the three phases, stop propagation, and use event delegation on a list | intermediate | plan |
| 18 | The event loop and timers | explain the call stack, the task queue and microtasks, use `setTimeout` and `setInterval`, and predict the order of timer and promise callbacks | advanced | plan |
| 19 | Callbacks and promises | say what callback hell is, say what the three promise states are, chain `then`, `catch` and `finally`, and use `Promise.all`, `race` and `allSettled` | intermediate | plan |
| 20 | async and await | write `async` functions, handle errors with `try` and `catch`, and run requests in sequence and in parallel | intermediate | plan |
| 21 | fetch and HTTP in the browser | use `fetch` with methods, headers and a body, check `response.ok`, cancel with `AbortController`, say why a 404 does not reject, and recognise `XMLHttpRequest` in old code | beginner | plan |
| 22 | JSON | use `JSON.parse` and `JSON.stringify`, say what JSON cannot hold, and handle bad JSON | beginner | plan |
| 23 | Error handling | use `try`, `catch`, `finally` and `throw`, know the built-in error types, write a custom error, and show an error to the user | beginner | plan |
| 24 | Browser storage | use `localStorage`, `sessionStorage` and cookies, say how they differ, and say what must never be stored there | — | plan |
| 25 | Forms and user input | read a form with `FormData`, handle `submit` with `preventDefault`, and use the constraint validation API | — | extra |
| 26 | Browser APIs | use `URL` and `URLSearchParams`, `history`, `IntersectionObserver`, timers and `requestAnimationFrame` | — | extra |
| 27 | Security basics in JavaScript | say how `innerHTML` and `eval` lead to XSS in the DOM, and why not to keep secrets in front-end code | — | plan |
| 28 | Debugging and DevTools | use the console, breakpoints and stack traces to find a bug, and use DevTools to find a memory leak or a slow function | intermediate | plan |
| 29 | Memory management | describe the memory lifecycle, say how garbage collection decides what to free, and name common causes of memory leaks | advanced | extra |
| 30 | Performance and the main thread | say what blocks the main thread, use debouncing and throttling, and know when a worker helps | — | extra |
| 31 | Tooling and packages | use `npm` and `package.json`, and say what a bundler, linter and formatter do | — | extra |
| 32 | Testing basics | write a small unit test with an assertion, and say what makes a function easy to test | — | extra |
| 33 | Regular expressions | read and write simple patterns, and use `match`, `test` and `replace` | — | extra |

Parked, not in the list: TypeScript, Node.js and back-end JavaScript, frameworks other than React, and the bitwise, comma and BigInt operators.

## React

The libraries are in their own section below, "React ecosystem".

| # | Topic | I can... | Tag |
|---|---|---|---|
| 1 | What React is and why | say what React is for, what declarative UI means, how components break a page up, and when plain JavaScript is enough | plan |
| 2 | Setting up a project | create a project with a build tool such as Vite, run the dev server, read the project structure, and say what `npm` scripts do | plan |
| 3 | JSX | write JSX with expressions, `className`, fragments and self-closing tags, and say what JSX compiles to and why it escapes values | plan |
| 4 | Components and props | write function components, pass props and `children`, compose components, and say why props are read-only | plan |
| 5 | Composition patterns | compose with `children`, recognise render props and higher-order components in older code, and say why hooks and composition replaced them | extra |
| 6 | Thinking in React | break a design into a component tree, build a static version first, and find the minimal state | plan |
| 7 | Rendering lists and keys | render a list with `map`, choose a stable `key`, and say what goes wrong with index keys | plan |
| 8 | Conditional rendering | render different output with `&&`, ternaries and early returns, and avoid the `0` rendering bug | plan |
| 9 | State with useState | add state, say when state versus props versus a variable, update with a function, treat state as immutable, and explain why updates are batched | plan |
| 10 | Rendering and re-rendering | say what triggers a render, the difference between render and commit, and why keys and state position matter | extra |
| 11 | Events and handlers | pass handlers to elements, read the event object, and say why you pass a function and don't call it | plan |
| 12 | Forms and controlled inputs | build a controlled input, handle `submit` with `preventDefault`, say when an uncontrolled input is fine, and say what a form library such as React Hook Form adds | plan |
| 13 | Sharing state and data flow | lift state up to a common parent, pass it down and call back up, and explain one-way data flow | plan |
| 14 | Filtering and derived state | filter and sort a list from state without storing the result, and say why duplicated state goes out of sync | plan |
| 15 | Effects with useEffect | say what an effect is for, describe the component lifecycle (mount, update, unmount) in terms of effects, write the dependency array, clean up, and explain why strict mode runs effects twice in development | plan |
| 16 | Fetching data in React | load data with an effect, show loading and error states, ignore or cancel stale responses, and say what a data library such as TanStack Query, SWR or Axios adds | plan |
| 17 | Refs and the DOM | use `useRef` to reach a DOM node or hold a value, move focus, and say when a ref is the wrong tool | extra |
| 18 | Hooks and custom hooks | state the rules of hooks, write a custom hook, and say what it shares and what it does not | extra |
| 19 | Context | create and use context, say when it is better than passing props, and name its cost | extra |
| 20 | Reducers | use `useReducer` for state with several related changes, and say when `useState` is simpler | extra |
| 21 | React accessibility | use semantic elements in JSX, label inputs, manage focus on route or dialog changes, support the keyboard, and announce changes with live regions | plan |
| 22 | Styling in React | style with CSS files, class names and inline `style`, and say what CSS Modules and utility classes change | extra |
| 23 | Performance basics | say when `memo`, `useMemo` and `useCallback` help and when they are noise, and use the profiler to find a slow render | extra |
| 24 | Error states and boundaries | show errors for failed requests, and say what an error boundary catches and what it does not | extra |
| 25 | Suspense and portals | say what `Suspense` is for, render a modal into another place in the DOM with a portal, and keep focus and the keyboard working | extra |
| 26 | Routing basics | say what client-side routing is, define routes and links, and read URL parameters | extra |
| 27 | Security in React | say what React escapes and what `dangerouslySetInnerHTML` bypasses, avoid unsafe `href` values, and keep secrets out of the bundle | plan |
| 28 | Testing components | write a test that renders a component and checks what a user sees, and say why testing behaviour beats testing implementation | extra |
| 29 | Debugging React | use React DevTools and StrictMode warnings to find a bug, and read the component stack in an error | plan |
| 30 | Small project: a filterable list | build a small accessible filterable list by hand (no AI) in `practice/`, and explain each design choice | plan |

Parked, not in the list: Next.js and server components, server APIs, TypeScript and Zod, GraphQL, state libraries in depth, end-to-end testing (Playwright, Cypress), animation libraries, and React Native. See the ecosystem section below for the libraries.

## React ecosystem (optional, not tracked on the map)

A reference for the libraries around React, not a list to master. Study a group only when a project needs it. The picks and alternatives are as I read the marks on your React roadmap (purple is the recommended pick, green is an alternative). A group is tracked on the map only if you move it into the React list above.

| Group | What it is for | Roadmap picks | Alternatives |
|---|---|---|---|
| Build tools | creating and running a project | Vite | |
| Routers | client-side routing | React Router | TanStack Router |
| State management | state shared across many components | Zustand, Jotai | MobX, Context |
| Writing CSS | styling components | Tailwind CSS | CSS Modules, Panda CSS |
| Component libraries | ready-made styled components | shadcn/ui | Material UI, Chakra UI |
| Headless components | behaviour and accessibility without styles | Base UI, Radix UI | React Aria, Ark UI |
| API calls: REST | fetching, caching and syncing server data | TanStack Query | Axios, SWR, RTK Query |
| API calls: GraphQL | querying a GraphQL server | Apollo | Relay, urql |
| Testing | unit, component and end-to-end tests | Vitest, Playwright, React Testing Library | Jest, Cypress |
| Forms | form state and validation | React Hook Form | Formik, Formish |
| Frameworks | routing, server rendering and a full project setup | Next.js, Astro | React Router |
| Types and validation | catching type and data errors | TypeScript, Zod | Valibot |
| Animation | motion and transitions | Framer Motion | react-spring, GSAP |
| Mobile | native mobile apps | React Native | |

## HTTP and the web

The lower layers (DNS, TCP/IP, TLS, IP addressing) are in the **Networking** subject, in the `networking/` folder, which comes later.

| # | Topic | I can... | Tag |
|---|---|---|---|
| 1 | URLs | split a URL into scheme, host, port, path, query and fragment, say which parts reach the server and which do not, and explain URL encoding | plan |
| 2 | HTTP messages | read a raw request and response: request line, status line, headers and body | plan |
| 3 | HTTP methods | choose `GET`, `POST`, `PUT`, `PATCH` and `DELETE`, and say what safe and idempotent mean | plan |
| 4 | Status codes | say what the 2xx, 3xx, 4xx and 5xx families mean, and the common codes (200, 301, 302, 304, 400, 401, 403, 404, 500, 503) and what to do about each | plan |
| 5 | Headers | use and read `Content-Type`, `Accept`, `Authorization`, `Host`, `User-Agent` and `Location`, and say which side sets each | plan |
| 6 | HTTP caching | use `Cache-Control`, `ETag` and conditional requests, say what a CDN caches, and say how to bust a cache | plan |
| 7 | Cookies and sessions | explain `Set-Cookie` and `Cookie`, the `HttpOnly`, `Secure` and `SameSite` attributes, and the difference between a session cookie and a token | plan |
| 8 | CORS and the same-origin policy | define an origin, say what the same-origin policy blocks, explain a preflight request, and fix a CORS error the right way | plan |
| 9 | HTTP/1.1, HTTP/2 and HTTP/3 | say what keep-alive, multiplexing and header compression fix, and what QUIC changes | plan |
| 10 | HSTS and enforcing HTTPS | say what `Strict-Transport-Security` does, what it protects against, and what the preload list is | plan |
| 11 | How browsers load a page | describe parsing, render-blocking resources, the critical path from bytes to pixels, what `defer`, `async` and `preload` change, and what the Core Web Vitals measure | plan |
| 12 | Browser-side attacks and defences | say how XSS, CSRF, clickjacking and a man-in-the-middle work, and which defence stops each | plan |
| 13 | Security headers | say what `Content-Security-Policy`, `X-Content-Type-Options`, `Referrer-Policy` and `frame-ancestors` do | plan |
| 14 | Network DevTools | read the Network tab: the waterfall, timings, headers, payload and cache status, throttle the connection, and copy a request as curl | plan |
| 15 | Redirects | tell 301, 302, 307 and 308 apart, and say how redirect chains hurt | extra |
| 16 | Compression and content types | say how gzip and Brotli work in transit, and choose a `Content-Type` and encoding | extra |
| 17 | REST and JSON APIs | design a resource URL, pick methods and status codes for an API, and say what pagination and idempotency are for | extra |
| 18 | Authentication basics | compare cookies and bearer tokens, outline OAuth at a high level, and say why you do not store tokens carelessly | extra |
| 19 | Real-time: WebSockets and server-sent events | say when to use a WebSocket, server-sent events or polling | extra |

Parked, not in the list: load balancing, scaling and system design (systems sessions).
