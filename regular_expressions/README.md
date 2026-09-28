# Regular Expressions

## Description

Ruby scripts that use regular expressions to match and extract patterns from text. Each script accepts one command-line argument, applies a regex to it, and prints the result. The project covers literal matching, repetition tokens (`?`, `*`, `{n,m}`), anchors, character classes, and a log-parsing exercise.

## Requirements

- All scripts are written in Ruby
- All scripts are executable
- The first line of every script is `#!/usr/bin/env ruby`
- Each script accepts one argument and passes it to a regular expression matching method

## Tasks

| File | Description |
| --- | --- |
| `0-simply_match_school.rb` | Matches every occurrence of `School` |
| `1-repetition_token_0.rb` | Matches `hbt{2,5}n`: `t` repeated 2 to 5 times |
| `2-repetition_token_1.rb` | Matches `hb?tn`: `b` is optional |
| `3-repetition_token_2.rb` | Matches `hbt{1,5}n`: `t` repeated 1 to 5 times |
| `4-repetition_token_3.rb` | Matches `hbt*n`: `t` repeated 0 or more times, no square brackets |
| `5-beginning_and_end.rb` | Matches a string starting with `h`, ending with `n`, with any single character between |
| `6-phone_number.rb` | Matches a 10 digit phone number |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Extracts only the capital letters |
| `8-textme.rb` | Parses a TextMe log line into `[SENDER],[RECEIVER],[FLAGS]` |

## Usage

```bash
./<script_name>.rb "<argument>"
```

## Author

acyubahiroo
