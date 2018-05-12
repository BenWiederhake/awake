# awake

> Helps you prove to a third party that you can communicate with another "instance" of them.

Assume you are [Michael Britten in the series "Awake"](https://www.imdb.com/title/tt1839683/?ref_=fn_al_tt_2),
and you want to prove to someone (i.e., the IT guy), that you can communicate with a different version of that IT guy.

Alternate realities already make everything hard, so I'll stick to this concrete example.
If you haven't seen the series yet, see the short guide that explains the roles
in an objective fashion.

This repository is spoiler-free (if you have seen episode 1),
because I haven't finished watching because I was
[nerd-sniped](https://xkcd.com/356/) and needed to write this. :-)

## Table of Contents

- [Role Guide and Setup](#role-guide-and-setup)
- [How to Use as Michael Britten](#how-to-use-as-michael-britten)
- [How to Use as Dr. John Lee](#how-to-use-as-dr-john-lee)
- [Design Criteria and Rationale](#design-criteria-and-rationale)
- [TODOs](#todos)
- [Contribute](#todos)
- [License](#license)

## Role Guide and Setup

**Michael Britten** is a guy who wakes up alternatingly in two different realities.
In the series this started because of a car accident, and the realities are identical
or extremely similar up to that point.

**Hannah Britten** and **Rex Britten** are the wife and son, respectively, of Michael Britten.
They are the key difference between the two realities:
In one reality, Hannah dies in the accident and Rex lives;
in the other, Hannah lives and Rex dies in the accident.

**Dr. John Lee** is someone that Michael Britten wants to convince of this.
(In the series he is a lot more relaxed about this, but I would do exactly that.)
I'm going to assume that Dr. John Lee has lots of technical capabilities,
but of course he should hire/ask a technically-minded person he knows and can rely upon.

This entire thing hinges on these things:
- Dr. John Lee generated a secret key *before* the accident.
  This secret key must have stayed secret in both realities.
- Dr. John Lee has no reason to distrust HMAC, i.e., there is no reason why
  Michael Britten should be able to forge a HMAC signature.
- The car accident happened during or after the year 1997. See [Design Criteria and Rationale](#design-criteria-and-rationale).

These clearly hold in the series, and should also hold in most similar scenarios.

## How to Use as Michael Britten

Obviously, Dr. John Lee first needs to be convinced to participate in this.
Mentioning the following should make it easier: Dr. John Lee can essentially
choose the message to be signed, so if Michael Britten is wrong/crazy/insane,
nothing is lost.  In all cases, the secret stays secret.

If the accident happend after May 2018, you're done: just point to the next section,
[How to Use as Dr. John Lee](#how-to-use-as-dr-john-lee), and follow Dr. John Lee's instructions.
The remainder of this section assumes that you can see this document only in one reality.

As an extra step, to make sure that all the cryptographic processes stayed the same, tell him the following:

> The `HMAC_SHA1` of the empty key and the empty message is some hard-to-remember letters-and-numbers-thing,
> which starts with `fbdb1d`.  Because I can't easily remember lots of letters-and-numbers all the time,
> I will use the PGP wordlist for that.  With it, the empty-key-empty-message-thing becomes
> `watchword suspicious Belfast bravado beaming pedigree`.
> Please first verify that the realities don't differ in this regard.

This also helps Dr. John Lee in testing whether he is using all the tools correctly.

Next, find a "secret" that Dr. John Lee still remembers in both realities, and chose before the accident.
The time of choice is important, as it needs to be identical (not just similar) in both realities.

Don't ask Dr. John Lee to reveal it.  Instead, try to find out a public part of the secret.
For example "it's the passphrase for my backups" or something.
And then make sure that both instances of Dr. John Lee know which secret is meant,
and especially the "how".

Next, ask both instances of him to sign a short message,
something like `Hannah died in the accident and Rex lives` in one reality,
and `Hannah lives and Rex died in the accident` in the other.
Keep it as simple as possible!

Serioulsly: Keep the signed messages as simple as possible, in order to ensure unique, clear,
and unambiguous reproduction in the other universe.
Ideally, tell Dr. John Lee that you're going to show up with the signature for the message from the other reality,
and he should understand why uniqueness and unambiguity is so important.

Ask for the signature in some form that you can transport between the realities.
As already introduced above, I suggest HMAC-SHA1 and PGP wordlist,
because they have been defined before the accident, and allow for relatively easy memoriziation,
and contain "just the right amount" of error correction.

If you follow this advice, you now need to memorize something like this for each reality:

> spindle travesty atlas miracle beaming Jamaica facial butterfat framework determine flagpole cellulose goggles backwater aimless fascinate commence revolver dwelling molasses

I know, that's a lot, but this volume is the absolute minimum to ensure cryptographic security.
Less than this is just not meaningful.

In case you're wondering, this is the signature for the message `Hannah died in the accident and Rex lives\n` and the key `My secret\n`.
Note that capitalization and special characters are significant!

With this knowledge, you can approach the Dr. John Lee of the "opposite" universe, and give him the following:
- The message, absolutely verbatim, including capitalization, punctuation, spaces, everything.
  Ideally, Dr. John Lee chose something simple like "everything lowercase except names, no punctuation, no newlines".
- The signature ("spindle travesty atlas …").  Here some minor mistakes don't break much, but you should try your absolute best to nail it on your first try.

I suggest spending some time to go back and forth between realities and writing down the "opposite" signature step by step.

With the message and signature, Dr. John Lee now can verify that the signature is, indeed, a signature.
The most reasonable outcomes are:
- You did a mistake.  If Dr. John Lee is really nice (he shouldn't be), he might even tell you whether the message
  or the signature seems to be the problem.  If it's the signature and you're only off by a little,
  Dr. John Lee might notice and fix this for you.
- Dr. John Lee made a mistake.  To rule this out, we made this test of "watchword suspicious Belfast" initially, so this is unlikely.
- Dr. John Lee accuses you of knowing his secret already.  You could try again with a different secret if you want,
  or simply prove it to a different person.
- Dr. John Lee accepts that you can communicate with a different version of Dr. John Lee who knows exactly the same secret.  Success!

Good luck.  I hope your memory is good.

Note that if the computer expert is well accredited, this could even be a proof to other people.

## How to Use as Dr. John Lee

Ask Michael Britten when the accident happened.  Using `HMAC-SHA1` and the PGP wordlist is safe from mid-1996 onwards,
but for extra security you might want to go for `HMAC-SHA512` or something.
Be gentle on Michael Britten, he has to memorize all this stuff.

First, run the following, to make sure your python interpreter is set up correctly:

    $ ./awake.py /dev/null /dev/null
    INFO: keylen=0, msglen=0
    watchword suspicious Belfast bravado beaming pedigree glucose antenna checkup disable klaxon getaway seabird businessman seabird Galveston guidance guitarist apple breakaway

This is the value of `HMAC-SHA1('', '')`, encoded in the PGP word list.

Next, you need to give the following pieces of information to Michael Britten:
- An easily identifiable secret that you generated **before** the accident.  For example: the passphrase to my backup partition.
- The message: keep it easy, because the other "you" has to end up with a bit-identical string.  For example: "Hannah died in the accident and Rex lives"
- The signature: run `./awake.py secret_file message_file`, for example: "spindle travesty atlas miracle beaming Jamaica facial butterfat framework determine flagpole cellulose goggles backwater aimless fascinate commence revolver dwelling molasses"
- That verbatim-ness is extremely important.  Let him repeat the secret-description, message, and signature until he gets it right.

A few days later (or maybe tomorrow), Michael Britten will come back to you with a different message and a signature for it.
As `HMAC-SHA1` is deterministic, you can just generate a "new" signature for it, and check whether the signatures are identical.
Try to cut Michael some slack, so if a single word is missing or wrong, you may still want to consider the signature as correct.

This does not impede security too much, as the message is too simple for this kind of manipulation (a nonce in the message would stick out like a sore thumb), and the kind and position of the error is immediately obvious (PGP wordlist encodes even/oddness of each byte).
So if you ignore up to one error, security is reduced from 180 (90) bits to 172 (86) bits.

Good luck, and don't get institutionalized yourself!  ;-)

If you want to increase the security level, just change this line:

    signature_bin = hmac.new(key, message, hashlib.sha1).digest()

to:

    signature_bin = hmac.new(key, message, hashlib.sha512).digest()

Now Michael Britten has to memorize so much more, but also can make a few more mistakes.

## Design Criteria and Rationale

The less crypto-stuff I design,
[the](https://security.stackexchange.com/questions/18197/why-shouldnt-we-roll-our-own?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa) [better](https://twitter.com/search?q=roll%20your%20own%20crypto&src=typd).
 So obviously, I should go with existing building blocks.

The main goal is authentication.  So any kind of
[Message Authentication Code](https://en.wikipedia.org/wiki/Message_authentication_code) is ideal,
because encryption solves the wrong problem (and does not imply authentication).

Next, these building blocks absolutely *must* already exist before the accident,
since we really can't afford the chance that they have been invented in slightly different ways,
e.g. using the square roots of 2, 3, 5 and 7 instead of [the square roots of 2, 3, 5 and 10](https://en.wikipedia.org/wiki/SHA-1#SHA-1_pseudocode).
Nobody can expect Michael Britten to find and explain
all the differences between Keccak-Hannah-died and Keccak-Rex-died.
I didn't have a specific year in mind, but I picked the oldest one
that is still regarded secure, namely: [`HMAC-SHA1`](https://en.wikipedia.org/wiki/HMAC#Examples).
This kinda excludes public key algorithms, as these are newer (and require more communcation).

Note that this is largely unaffected by the SHAppening,
[SHAttered](https://en.wikipedia.org/wiki/SHA-1#SHAttered_%E2%80%93_first_public_collision),
or similar attacks, as it requires
especially prepared messages and some nonces in the code-to-be-hashed.
In order to achieve this here, the nonces are either the SHA1 of key and message each
(more difficult than the original problem),
or the message itself contains these, which would immediately be obvious to Dr. John Lee.

The signature needs to be transferred between realities.
However, Micheal Britten can't be expected to flawlessly memorize a 160-bit hexadecimal string,
even though 160-bit is technically rather short.
I decided to use the [PGP wordlist](https://en.wikipedia.org/wiki/PGP_word_list), because it also solves another problem in passing:

Error correction.  Michael Britten has to memorize at least 20 random English words worth of information,
no matter what the encoding.  Errors will happen, both to the message and the signature.
As we're using the PGP wordlist, each byte is additionally tagged with its positional parity.
This helps Dr. John Lee to immediately identify whether a word was omitted and where (because there is an odd-odd or even-even subsequence),
or a single word was misremembered.
It also makes checking for validity easy, as he can easily scan whether "most" of the signature matches.

Finally, error correction to the message.  MISSING

In short, the design criteria were:
- Ease of data transfer between the realities (Michael Britten has limited memory for "random letters and numbers")
- Reconstructability (Maybe one Dr. John Lee has no access to this document.)
- Reliability (There is no way this can go wrong in practice, because my assumptions are few.)
- Safety (There is no way this can go wrong in theory, because the building blocks already have been analyzed.)
- Believability (After convincing Dr. John Lee, Michael Britten may want to convice others by pointing to Dr. John Lee.)

## TODOs

- Is there an even easier approach?
- Is there a better way to convince Dr. John Lee that there is absolutely no way his secret could get leaked?
- Could Dr. John Lee use a "newer" secret in some form?
- Document the idea about CRC32-ing the message.

## Contribute

PRs are very welcome, but please only solve actual problems.

In particular, don't add "features" to the program that make it "more secure"
but violate some other design criterion, like ease of data transfer or reconstructability.
For example, saying "just emulate an ssh session, duh" is a bad idea.

## License

MIT License, see file `LICENSE`.

Rationale: As permissive as possible.  If you need a different license,
for example WTFPL, just contact me.
