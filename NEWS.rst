4.58.5 (released 2025-07-03)
----------------------------

- [feaLib] Don't try to combine ligature & multisub rules (#3874).
- [feaLib/ast] Use weakref proxies to avoid cycles in visitor (#3873).
- [varLib.instancer] Fixed instancing CFF2 fonts where VarData contains more than 64k items (#3858).

4.58.4 (released 2025-06-13)
----------------------------

- [feaLib] Allow for empty MarkFilter & MarkAttach sets (#3856).

4.58.3 (released 2025-06-13)
----------------------------

- [feaLib] Fixed iterable check for Python 3.13.4 and newer (#3854, #3855).

4.58.2 (released 2025-06-06)
----------------------------

- [ttLib.reorderGlyphs] Handle CFF2 when reordering glyphs (#3852)
- [subset] Copy name IDs in use before scrapping or scrambling them for webfonts (#3853)

4.58.1 (released 2025-05-28)
----------------------------

- [varLib] Make sure that fvar named instances only reuse name ID 2 or 17 if they are at the default location across all axes, to match OT spec requirement (#3831).
- [feaLib] Improve single substitution promotion to multiple/ligature substitutions, fixing a few bugs as well (#3849).
- [loggingTools] Make ``Timer._time`` a static method that doesn't take self, makes it easier to override (#3836).
- [featureVars] Use ``None`` for empty ConditionSet, which translates to a null offset in the compiled table (#3850).
- [feaLib] Raise an error on conflicting ligature substitution rules instead of silently taking the last one (#3835).
- Add typing annotations to T2CharStringPen (#3837).
- [feaLib] Add single substitutions that were promoted to multiple or ligature substitutions to ``aalt`` feature (#3847).
- [featureVars] Create a default ``LangSys`` in a ``ScriptRecord`` if missing when adding feature variations to existing GSUB later in the build (#3838).
- [symfont] Added a ``main()``.
- [cffLib.specializer] Fix rmoveto merging when blends used (#3839, #3840).
- [pyftmerge] Add support for cmap format 14 in the merge tool (#3830).
- [varLib.instancer/cff2] Fix vsindex of Private dicts when instantiating (#3828, #3232).
- Update text file read to use UTF-8 with optional BOM so it works with e.g. Windows Notepad.exe (#3824).
- [varLib] Ensure that instances only reuse name ID 2 or 17 if they are at the default location across all axes (#3831).
- [varLib] Create a dflt LangSys in a ScriptRecord when adding variations later, to fix an avoidable crash in an edge case (#3838).

4.58.0 (released 2025-05-10)
----------------------------

- Drop Python 3.8, require 3.9+ (#3819)
- [HVAR, VVAR] Prune unused regions when using a direct mapping (#3797)
- [Docs] Improvements to ufoLib documentation (#3721)
- [Docs] Improvements to varLib documentation (#3727)
- [Docs] Improvements to Pens and pen-module documentation (#3724)
- [Docs] Miscellany updates to docs (misc modules and smaller modules) (#3730)
- [subset] Close codepoints over BiDi mirror variants. (#3801)
- [feaLib] Fix serializing ChainContextPosStatement and
  ChainContextSubstStatement in some rare cases (#3788)
- [designspaceLib] Clarify user expectations for getStatNames (#2892)
- [GVAR] Add support for new `GVAR` table (#3728)
- [TSI0, TSI5] Derive number of entries to decompile from data length (#2477)
- [ttLib] Fix `AttributeError` when reporting table overflow (#3808)
- [ttLib] Apply rounding more often in getCoordinates (#3798)
- [ttLib] Ignore component bounds if empty (#3799)
- [ttLib] Change the separator for duplicate glyph names from "#" to "." (#3809)
- [feaLib] Support subtable breaks in CursivePos, MarkBasePos, MarkToLigPos and
  MarkToMarkPos lookups (#3800, #3807)
- [feaLib] If the same lookup has single substitutions and ligature
  substitutions, upgrade single substitutions to ligature substitutions with
  one input glyph (#3805)
- [feaLib] Correctly handle <NULL> in single pos lookups (#3803)
- [feaLib] Remove duplicates from class pair pos classes instead of raising an
  error (#3804)
- [feaLib] Support creating extension lookups using useExtenion lookup flag
  instead of silently ignoring it (#3811)
- [STAT] Add typing for the simpler STAT arguments (#3812)
- [otlLib.builder] Add future import for annotations (#3814)
- [cffLib] Fix reading supplement encoding (#3813)
- [voltLib] Add some missing functionality and fixes to voltLib and VoltToFea,
  making the conversion to feature files more robust. Add also `fonttools
  voltLib` command line tool to compile VOLT sources directly (doing an
  intermediate fea conversion internally) (#3818)
- [pens] Add some PointPen annotations (#3820)

4.57.0 (released 2025-04-03)
----------------------------

- [ttLib.__main__] Add `--no-recalc-timestamp` flag (#3771)
- [ttLib.__main__] Add `-b` (recalcBBoxes=False) flag (#3772)
- [cmap] Speed up glyphOrder loading from cmap (#3774)
- [ttLib.__main__] Improvements around the `-t` flag (#3776)
- [Debg] Fix parsing from XML; add roundtrip tests (#3781)
- [fealib] Support \*Base.MinMax tables (#3783, #3786)
- [config] Add OPTIMIZE_FONT_SPEED (#3784)
- [varLib.hvar] New module to add HVAR table to the font (#3780)
- [otlLib.optimize] Fix crash when the provided TTF does not contain a `GPOS` (#3794)

4.56.0 (released 2025-02-07)
----------------------------

- [varStore] Sort the input todo list with the same sorting key used for the opimizer's output (#3767).
- [otData] Fix DeviceTable's ``DeltaValue`` repeat value which caused a crash after importing from XML and then compiling a GPOS containing Device tables (#3758).
- [feaLib] Make ``FeatureLibError`` pickleable, so client can e.g. use feaLib to can compile features in parallel with multiprocessing (#3762).
- [varLib/gvar] Removed workaround for old, long-fixed macOS bug about composite glyphs with all zero deltas (#1381, #1788).
- [Docs] Updated ttLib documentation, beefed up TTFont and TTGlyphSet explanations (#3720).

4.55.8 (released 2025-01-29)
----------------------------

- [MetaTools] Fixed bug in buildUCD.py script whereby the first non-header line of some UCD text file was being skipped. This affected in particular the U+00B7 (MIDDLE DOT) entry of ScriptExtensions.txt (#3756).

4.55.7 (released 2025-01-28)
----------------------------

- Shorten the changelog included in PyPI package description to accommodate maximum length limit imposed by Azure DevOps. No actual code changes since v4.55.6 (#3754).

4.55.6 (released 2025-01-24)
----------------------------

- [glyf] Fixed regression introduced in 4.55.5 when computing bounds of nested composite glyphs  with transformed components (#3752).

4.55.5 (released 2025-01-23)
----------------------------

- [glyf] Fixed recalcBounds of transformed components with unrounded coordinates (#3750).
- [feaLib] Allow duplicate script/language statements (#3749).

4.55.4 (released 2025-01-21)
----------------------------

- [bezierTools] Fixed ``splitCubicAtT`` sometimes not returning identical start/end points as result of numerical precision (#3742, #3743).
- [feaLib/ast] Fixed docstring of ``AlternateSubstStatement`` (#3735).
- [transform] Typing fixes (#3734).

4.55.3 (released 2024-12-10)
----------------------------

- [Docs] fill out ttLib table section [#3716]
- [feaLib] More efficient inline format 4 lookups [#3726]

4.55.2 (released 2024-12-05)
----------------------------

- [Docs] update Sphinx config (#3712)
- [designspaceLib] Allow axisOrdering to be set to zero (#3715)
- [feaLib] Don’t modify variable anchors in place (#3717)

4.55.1 (released 2024-12-02)
----------------------------

- [ttGlyphSet] Support VARC CFF2 fonts (#3683)
- [DecomposedTransform] Document and implement always skewY == 0 (#3697)
- [varLib] "Fix" cython iup issue? (#3704)
- Cython minor refactor (#3705)


4.55.0 (released 2024-11-14)
----------------------------

- [cffLib.specializer] Adjust stack use calculation (#3689)
- [varLib] Lets not add mac names if the rest of name doesn't have them (#3688)
- [ttLib.reorderGlyphs] Update CFF table charstrings and charset (#3682)
- [cffLib.specializer] Add cmdline to specialize a CFF2 font (#3675, #3679)
- [CFF2] Lift uint16 VariationStore.length limitation (#3674)
- [subset] consider variation selectors subsetting cmap14 (#3672)
- [varLib.interpolatable] Support CFF2 fonts (#3670)
- Set isfinal to true in XML parser for proper resource cleanup (#3669)
- [removeOverlaps] Fix CFF CharString width (#3659)
- [glyf] Add optimizeSize option (#3657)
- Python 3.13 support (#3656)
- [TupleVariation] Optimize for loading speed, not size (#3650, #3653)


4.54.1 (released 2024-09-24)
----------------------------

- [unicodedata] Update to Unicode 16
- [subset] Escape ``\\`` in doc string

4.54.0 (released 2024-09-23)
----------------------------

- [Docs] Small docs cleanups by @n8willis (#3611)
- [Docs] cleanup code blocks by @n8willis (#3627)
- [Docs] fix Sphinx builds by @n8willis (#3625)
- [merge] Minor fixes to documentation for merge by @drj11 (#3588)
- [subset] Small tweaks to pyftsubset documentation by @RoelN (#3633)
- [Tests] Do not require fonttools command to be available by @behdad (#3612)
- [Tests] subset_test: add failing test to reproduce issue #3616 by @anthrotype (#3622)
- [ttLib] NameRecordVisitor: include whole sequence of character variants' UI labels, not just the first by @anthrotype (#3617)
- [varLib.avar] Reconstruct mappings from binary by @behdad (#3598)
- [varLib.instancer] Fix visual artefacts with partial L2 instancing by @Hoolean (#3635)
- [varLib.interpolatable] Support discrete axes in .designspace by @behdad (#3599)
- [varLib.models] By default, assume OpenType-like normalized space by @behdad (#3601)

4.53.1 (released 2024-07-05)
----------------------------

- [feaLib] Improve the sharing of inline chained lookups (#3559)
- [otlLib] Correct the calculation of OS/2.usMaxContext with reversed chaining contextual single substitutions (#3569)
- [misc.visitor] Visitors search the inheritance chain of objects they are visiting (#3581)

4.53.0 (released 2024-05-31)
----------------------------

- [ttLib.removeOverlaps] Support CFF table to aid in downconverting CFF2 fonts (#3528)
- [avar] Fix crash when accessing not-yet-existing attribute (#3550)
- [docs] Add buildMathTable to otlLib.builder documentation (#3540)
- [feaLib] Allow UTF-8 with BOM when reading features (#3495)
- [SVGPathPen] Revert rounding coordinates to two decimal places by default (#3543)
- [varLib.instancer] Refix output filename decision-making  (#3545, #3544, #3548)

4.52.4 (released 2024-05-27)
----------------------------

- [varLib.cff] Restore and deprecate convertCFFtoCFF2 that was removed in 4.52.0
  release as it is used by downstream projects (#3535).

4.52.3 (released 2024-05-27)
----------------------------

- Fixed a small syntax error in the reStructuredText-formatted NEWS.rst file
  which caused the upload to PyPI to fail for 4.52.2. No other code changes.

4.52.2 (released 2024-05-27)
----------------------------

- [varLib.interpolatable] Ensure that scipy/numpy output is JSON-serializable
  (#3522, #3526).
- [housekeeping] Regenerate table lists, to fix pyinstaller packaging of the new
  ``VARC`` table (#3531, #3529).
- [cffLib] Make CFFToCFF2 and CFF2ToCFF more robust (#3521, #3525).

4.52.1 (released 2024-05-24)
----------------------------

- Fixed a small syntax error in the reStructuredText-formatted NEWS.rst file
  which caused the upload to PyPI to fail for 4.52.0. No other code changes.

4.52.0 (released 2024-05-24)
----------------------------

- Added support for the new ``VARC`` (Variable Composite) table that is being
  proposed to OpenType spec (#3395). For more info:
  https://github.com/harfbuzz/boring-expansion-spec/blob/main/VARC.md
- [ttLib.__main__] Fixed decompiling all tables (90fed08).
- [feaLib] Don't reference the same lookup index multiple times within the same
  feature record, it is only applied once anyway (#3520).
- [cffLib] Moved methods to desubroutinize, remove hints and unused subroutines
  from subset module to cffLib (#3517).
- [varLib.instancer] Added support for partial-instancing CFF2 tables! Also, added
  method to down-convert from CFF2 to CFF 1.0, and CLI entry points to convert
  CFF<->CFF2 (#3506).
- [subset] Prune unused user name IDs even with --name-IDs='*' (#3410).
- [ttx] use GNU-style getopt to intermix options and positional arguments (#3509).
- [feaLib.variableScalar] Fixed ``value_at_location()`` method (#3491)
- [psCharStrings] Shorten output of ``encodeFloat`` (#3492).
- [bezierTools] Fix infinite-recursion in ``calcCubicArcLength`` (#3502).
- [avar2] Implement ``avar2`` support in ``TTFont.getGlyphSet()`` (#3473).

4.51.0 (released 2024-04-05)
----------------------------

- [ttLib] Optimization on loading aux fields (#3464).
- [ttFont] Add reorderGlyphs (#3468).

4.50.0 (released 2024-03-15)
----------------------------

- [pens] Added decomposing filter pens that draw components as regular contours (#3460).
- [instancer] Drop explicit no-op axes from TupleVariations (#3457).
- [cu2qu/ufo] Return set of modified glyph names from fonts_to_quadratic (#3456).

4.49.0 (released 2024-02-15)
----------------------------

- [otlLib] Add API for building ``MATH`` table (#3446)

4.48.1 (released 2024-02-06)
----------------------------

- Fixed uploading wheels to PyPI, no code changes since v4.48.0.

4.48.0 (released 2024-02-06)
----------------------------

- [varLib] Do not log when there are no OTL tables to be merged.
- [setup.py] Do not restrict lxml<5 any more, tests pass just fine with lxml>=5.
- [feaLib] Remove glyph and class names length restrictions in FEA (#3424).
- [roundingPens] Added ``transformRoundFunc`` parameter to the rounding pens to allow
  for custom rounding of the components' transforms (#3426).
- [feaLib] Keep declaration order of ligature components within a ligature set, instead
  of sorting by glyph name (#3429).
- [feaLib] Fixed ordering of alternates in ``aalt`` lookups, following the declaration
  order of feature references within the ``aalt`` feature block (#3430).
- [varLib.instancer] Fixed a bug in the instancer's IUP optimization (#3432).
- [sbix] Support sbix glyphs with new graphicType "flip" (#3433).
- [svgPathPen] Added ``--glyphs`` option to dump the SVG paths for the named glyphs
  in the font (0572f78).
- [designspaceLib] Added "description" attribute to ``<mappings>`` and ``<mapping>``
  elements, and allow multiple ``<mappings>`` elements to group ``<mapping>`` elements
  that are logically related (#3435, #3437).
- [otlLib] Correctly choose the most compact GSUB contextual lookup format (#3439).

4.47.2 (released 2024-01-11)
----------------------------

Minor release to fix uploading wheels to PyPI.

4.47.1 (released 2024-01-11)
----------------------------

- [merge] Improve help message and add standard command line options (#3408)
- [otlLib] Pass ``ttFont`` to ``name.addName`` in ``buildStatTable`` (#3406)
- [featureVars] Re-use ``FeatureVariationRecord``'s when possible (#3413)

4.47.0 (released 2023-12-18)
----------------------------

- [varLib.models] New API for VariationModel: ``getMasterScalars`` and
  ``interpolateFromValuesAndScalars``.
- [varLib.interpolatable] Various bugfixes and rendering improvements. In particular,
  add a Summary page in the front, and an Index and Table-of-Contents in the back.
  Change the page size to Letter.
- [Docs/designspaceLib] Defined a new ``public.fontInfo`` lib key, not used anywhere yet (#3358).

4.46.0 (released 2023-12-02)
----------------------------

- [featureVars] Allow to register the same set of substitution rules to multiple features.
  The ``addFeatureVariations`` function can now take a list of featureTags; similarly, the
  lib key 'com.github.fonttools.varLib.featureVarsFeatureTag' can now take a
  comma-separateed string of feature tags (e.g. "salt,ss01") instead of a single tag (#3360).
- [featureVars] Don't overwrite GSUB FeatureVariations, but append new records to it
  for features which are not already there. But raise ``VarLibError`` if the feature tag
  already has feature variations associated with it (#3363).
- [varLib] Added ``addGSUBFeatureVariations`` function to add GSUB Feature Variations
  to an existing variable font from rules defined in a DesignSpace document (#3362).
- [varLib.interpolatable] Various bugfixes and rendering improvements. In particular,
  a new test for "underweight" glyphs. The new test reports quite a few false-positives
  though. Please send feedback.

4.45.1 (released 2023-11-23)
----------------------------

- [varLib.interpolatable] Various bugfixes and improvements, better reporting, reduced
  false positives.
- [ttGlyphSet] Added option to not recalculate glyf bounds (#3348).

4.45.0 (released 2023-11-20)
----------------------------

- [varLib.interpolatable] Vastly improved algorithms. Also available now is ``--pdf``
  and ``--html`` options to generate a PDF or HTML report of the interpolation issues.
  The PDF/HTML report showcases the problematic masters, the interpolated broken
  glyph, as well as the proposed fixed version.

4.44.3 (released 2023-11-15)
----------------------------

- [subset] Only prune codepage ranges for OS/2.version >= 1, ignore otherwise (#3334).
- [instancer] Ensure hhea vertical metrics stay in sync with OS/2 ones after instancing
  MVAR table containing 'hasc', 'hdsc' or 'hlgp' tags (#3297).

4.44.2 (released 2023-11-14)
----------------------------

- [glyf] Have ``Glyph.recalcBounds`` skip empty components (base glyph with no contours)
  when computing the bounding box of composite glyphs. This simply restores the existing
  behavior before some changes were introduced in fonttools 4.44.0 (#3333).

4.44.1 (released 2023-11-14)
----------------------------

- [feaLib] Ensure variable mark anchors are deep-copied while building since they
  get modified in-place and later reused (#3330).
- [OS/2|subset] Added method to ``recalcCodePageRanges`` to OS/2 table class; added
  ``--prune-codepage-ranges`` to `fonttools subset` command (#3328, #2607).

4.44.0 (released 2023-11-03)
----------------------------

- [instancer] Recalc OS/2 AvgCharWidth after instancing if default changes (#3317).
- [otlLib] Make ClassDefBuilder class order match varLib.merger's, i.e. large
  classes first, then glyph lexicographic order (#3321, #3324).
- [instancer] Allow not specifying any of min:default:max values and let be filled
  up with fvar's values (#3322, #3323).
- [instancer] When running --update-name-table ignore axes that have no STAT axis
  values (#3318, #3319).
- [Debg] When dumping to ttx, write the embedded JSON as multi-line string with
  indentation (92cbfee0d).
- [varStore] Handle > 65535 items per encoding by splitting VarData subtable (#3310).
- [subset] Handle null-offsets in MarkLigPos subtables.
- [subset] Keep East Asian spacing fatures vhal, halt, chws, vchw by default (#3305).
- [instancer.solver] Fixed case where axisDef < lower and upper < axisMax (#3304).
- [glyf] Speed up compilation, mostly around ``recalcBounds`` (#3301).
- [varLib.interpolatable] Speed it up when working on variable fonts, plus various
  micro-optimizations (#3300).
- Require unicodedata2 >= 15.1.0 when installed with 'unicode' extra, contains UCD 15.1.

4.43.1 (released 2023-10-06)
----------------------------

- [EBDT] Fixed TypeError exception in `_reverseBytes` method triggered when dumping
  some bitmap fonts with `ttx -z bitwise` option (#3162).
- [v/hhea] Fixed UnboundLocalError exception in ``recalc`` method when no vmtx or hmtx
  tables are present (#3290).
- [bezierTools] Fixed incorrectly typed cython local variable leading to TypeError when
  calling ``calcQuadraticArcLength`` (#3288).
- [feaLib/otlLib] Better error message when building Coverage table with missing glyph (#3286).

4.43.0 (released 2023-09-29)
----------------------------

- [subset] Set up lxml ``XMLParser(resolve_entities=False)`` when parsing OT-SVG documents
  to prevent XML External Entity (XXE) attacks (9f61271dc):
  https://codeql.github.com/codeql-query-help/python/py-xxe/
- [varLib.iup] Added workaround for a Cython bug in ``iup_delta_optimize`` that was
  leading to IUP tolerance being incorrectly initialised, resulting in sub-optimal deltas
  (60126435d, cython/cython#5732).
- [varLib] Added new command-line entry point ``fonttools varLib.avar`` to add an
  ``avar`` table to an existing VF from axes mappings in a .designspace file (0a3360e52).
- [instancer] Fixed bug whereby no longer used variation regions were not correctly pruned
  after VarData optimization (#3268).
- Added support for Python 3.12 (#3283).

4.42.1 (released 2023-08-20)
----------------------------

- [t1Lib] Fixed several Type 1 issues (#3238, #3240).
- [otBase/packer] Allow sharing tables reached by different offset sizes (#3241, #3236).
- [varLib/merger] Fix Cursive attachment merging error when all anchors are NULL (#3248, #3247).
- [ttLib] Fixed warning when calling ``addMultilingualName`` and ``ttFont`` parameter was not
  passed on to ``findMultilingualName`` (#3253).

4.42.0 (released 2023-08-02)
----------------------------

- [varLib] Use sentinel value 0xFFFF to mark a glyph advance in hmtx/vmtx as non
  participating, allowing sparse masters to contain glyphs for variation purposes other
  than {H,V}VAR (#3235).
- [varLib/cff] Treat empty glyphs in non-default masters as missing, thus not participating
  in CFF2 delta computation, similarly to how varLib already treats them for gvar (#3234).
- Added varLib.avarPlanner script to deduce 'correct' avar v1 axis mappings based on
  glyph average weights (#3223).

4.41.1 (released 2023-07-21)
----------------------------

- [subset] Fixed perf regression in v4.41.0 by making ``NameRecordVisitor`` only visit
  tables that do contain nameID references (#3213, #3214).
- [varLib.instancer] Support instancing fonts containing null ConditionSet offsets in
  FeatureVariationRecords (#3211, #3212).
- [statisticsPen] Report font glyph-average weight/width and font-wide slant.
- [fontBuilder] Fixed head.created date incorrectly set to 0 instead of the current
  timestamp, regression introduced in v4.40.0 (#3210).
- [varLib.merger] Support sparse ``CursivePos`` masters (#3209).

4.41.0 (released 2023-07-12)
----------------------------

- [fontBuilder] Fixed bug in setupOS2 with default panose attribute incorrectly being
  set to a dict instead of a Panose object (#3201).
- [name] Added method to ``removeUnusedNameRecords`` in the user range (#3185).
- [varLib.instancer] Fixed issue with L4 instancing (moving default) (#3179).
- [cffLib] Use latin1 so we can roundtrip non-ASCII in {Full,Font,Family}Name (#3202).
- [designspaceLib] Mark <source name="..."> as optional in docs (as it is in the code).
- [glyf-1] Fixed drawPoints() bug whereby last cubic segment becomes quadratic (#3189, #3190).
- [fontBuilder] Propagate the 'hidden' flag to the fvar Axis instance (#3184).
- [fontBuilder] Update setupAvar() to also support avar 2, fixing ``_add_avar()`` call
  site (#3183).
- Added new ``voltLib.voltToFea`` submodule (originally Tiro Typeworks' "Volto") for
  converting VOLT OpenType Layout sources to FEA format (#3164).

4.40.0 (released 2023-06-12)
----------------------------

- Published native binary wheels to PyPI for all the python minor versions and platform
  and architectures currently supported that would benefit from this. They will include
  precompiled Cython-accelerated modules (e.g. cu2qu) without requiring to compile them
  from source. The pure-python wheel and source distribution will continue to be
  published as always (pip will automatically chose them when no binary wheel is
  available for the given platform, e.g. pypy). Use ``pip install --no-binary=fonttools fonttools``
  to expliclity request pip to install from the pure-python source.
- [designspaceLib|varLib] Add initial support for specifying axis mappings and build
  ``avar2`` table from those (#3123).
- [feaLib] Support variable ligature caret position (#3130).
- [varLib|glyf] Added option to --drop-implied-oncurves; test for impliable oncurve
  points either before or after rounding (#3146, #3147, #3155, #3156).
- [TTGlyphPointPen] Don't error with empty contours, simply ignore them (#3145).
- [sfnt] Fixed str vs bytes remnant of py3 transition in code dealing with de/compiling
  WOFF metadata (#3129).
- [instancer-solver] Fixed bug when moving default instance with sparse masters (#3139, #3140).
- [feaLib] Simplify variable scalars that don’t vary (#3132).
- [pens] Added filter pen that explicitly emits closing line when lastPt != movePt (#3100).
- [varStore] Improve optimize algorithm and better document the algorithm (#3124, #3127).
  Added ``quantization`` option (#3126).
- Added CI workflow config file for building native binary wheels (#3121).
- [fontBuilder] Added glyphDataFormat=0 option; raise error when glyphs contain cubic
  outlines but glyphDataFormat was not explicitly set to 1 (#3113, #3119).
- [subset] Prune emptied GDEF.MarkGlyphSetsDef and remap indices; ensure GDEF is
  subsetted before GSUB and GPOS (#3114, #3118).
- [xmlReader] Fixed issue whereby DSIG table data was incorrectly parsed (#3115, #2614).
- [varLib/merger] Fixed merging of SinglePos with pos=0 (#3111, #3112).
- [feaLib] Demote "Feature has not been defined" error to a warning when building aalt
  and referenced feature is empty (#3110).
- [feaLib] Dedupe multiple substitutions with classes (#3105).

4.39.4 (released 2023-05-10)
----------------------------

- [varLib.interpolatable] Allow for sparse masters (#3075)
- [merge] Handle differing default/nominalWidthX in CFF (#3070)
- [ttLib] Add missing main.py file to ttLib package (#3088)
- [ttx] Fix missing composite instructions in XML (#3092)
- [ttx] Fix split tables option to work on filenames containing '%' (#3096)
- [featureVars] Process lookups for features other than rvrn last (#3099)
- [feaLib] support multiple substitution with classes (#3103)

4.39.3 (released 2023-03-28)
----------------------------

- [sbix] Fixed TypeError when compiling empty glyphs whose imageData is None, regression
  was introduced in v4.39 (#3059).
- [ttFont] Fixed AttributeError on python <= 3.10 when opening a TTFont from a tempfile
  SpooledTemporaryFile, seekable method only added on python 3.11 (#3052).

4.39.2 (released 2023-03-16)
----------------------------

- [varLib] Fixed regression introduced in 4.39.1 whereby an incomplete 'STAT' table
  would be built even though a DesignSpace v5 did contain 'STAT' definitions (#3045, #3046).

4.39.1 (released 2023-03-16)
----------------------------

- [avar2] Added experimental support for reading/writing avar version 2 as specified in
  this draft proposal: https://github.com/harfbuzz/boring-expansion-spec/blob/main/avar2.md
- [glifLib] Wrap underlying XML library exceptions with GlifLibError when parsing GLIFs,
  and also print the name and path of the glyph that fails to be parsed (#3042).
- [feaLib] Consult avar for normalizing user-space values in ConditionSets and in
  VariableScalars (#3042, #3043).
- [ttProgram] Handle string input to Program.fromAssembly() (#3038).
- [otlLib] Added a config option to emit GPOS 7 lookups, currently disabled by default
  because of a macOS bug (#3034).
- [COLRv1] Added method to automatically compute ClipBoxes (#3027).
- [ttFont] Fixed getGlyphID to raise KeyError on missing glyphs instead of returning
  None. The regression was introduced in v4.27.0 (#3032).
- [sbix] Fixed UnboundLocalError: cannot access local variable 'rawdata' (#3031).
- [varLib] When building VF, do not overwrite a pre-existing ``STAT`` table that was built
  with feaLib from FEA feature file. Also, added support for building multiple VFs
  defined in Designspace v5 from ``fonttools varLib`` script (#3024).
- [mtiLib] Only add ``Debg`` table with lookup names when ``FONTTOOLS_LOOKUP_DEBUGGING``
  env variable is set (#3023).

4.39.0 (released 2023-03-06)
----------------------------

- [mtiLib] Optionally add `Debg` debug info for MTI feature builds (#3018).
- [ttx] Support reading input file from standard input using special `-` character,
  similar to existing `-o -` option to write output to standard output (#3020).
- [cython] Prevent ``cython.compiled`` raise AttributeError if cython not installed
  properly (#3017).
- [OS/2] Guard against ZeroDivisionError when calculating xAvgCharWidth in the unlikely
  scenario no glyph has non-zero advance (#3015).
- [subset] Recompute xAvgCharWidth independently of --no-prune-unicode-ranges,
  previously the two options were involuntarily bundled together (#3012).
- [fontBuilder] Add ``debug`` parameter to addOpenTypeFeatures method to add source
  debugging information to the font in the ``Debg`` private table (#3008).
- [name] Make NameRecord `__lt__` comparison not fail on Unicode encoding errors (#3006).
- [featureVars] Fixed bug in ``overlayBox`` (#3003, #3005).
- [glyf] Added experimental support for cubic bezier curves in TrueType glyf table, as
  outlined in glyf v1 proposal (#2988):
  https://github.com/harfbuzz/boring-expansion-spec/blob/main/glyf1-cubicOutlines.md
- Added new qu2cu module and related qu2cuPen, the reverse of cu2qu for converting
  TrueType quadratic splines to cubic bezier curves (#2993).
- [glyf] Added experimental support for reading and writing Variable Composites/Components
  as defined in glyf v1 spec proposal (#2958):
  https://github.com/harfbuzz/boring-expansion-spec/blob/main/glyf1-varComposites.md.
- [pens]: Added `addVarComponent` method to pen protocols' base classes, which pens can implement
  to handle varcomponents (by default they get decomposed) (#2958).
- [misc.transform] Added DecomposedTransform class which implements an affine transformation
  with separate translate, rotation, scale, skew, and transformation-center components (#2598)
- [sbix] Ensure Glyph.referenceGlyphName is set; fixes error after dumping and
  re-compiling sbix table with 'dupe' glyphs (#2984).
- [feaLib] Be cleverer when merging chained single substitutions into same lookup
  when they are specified using the inline notation (#2150, #2974).
- [instancer] Clamp user-inputted axis ranges to those of fvar (#2959).
- [otBase/subset] Define ``__getstate__`` for BaseTable so that a copied/pickled 'lazy'
  object gets its own OTTableReader to read from; incidentally fixes a bug while
  subsetting COLRv1 table containing ClipBoxes on python 3.11 (#2965, #2968).
- [sbix] Handle glyphs with "dupe" graphic type on compile correctly (#2963).
- [glyf] ``endPointsOfContours`` field should be unsigned! Kudos to behdad for
  spotting one of the oldest bugs in FT. Probably nobody has ever dared to make
  glyphs with more than 32767 points... (#2957).
- [feaLib] Fixed handling of ``ignore`` statements with unmarked glyphs to match
  makeotf behavior, which assumes the first glyph is marked (#2950).
- Reformatted code with ``black`` and enforce new code style via CI check (#2925).
- [feaLib] Sort name table entries following OT spec prescribed order in the builder (#2927).
- [cu2quPen] Add Cu2QuMultiPen that converts multiple outlines at a time in
  interpolation compatible way; its methods take a list of tuples arguments
  that would normally be passed to individual segment pens, and at the end it
  dispatches the converted outlines to each pen (#2912).
- [reverseContourPen/ttGlyphPen] Add outputImpliedClosingLine option (#2913, #2914,
  #2921, #2922, #2995).
- [gvar] Avoid expanding all glyphs unnecessarily upon compile (#2918).
- [scaleUpem] Fixed bug whereby CFF2 vsindex was scaled; it should not (#2893, #2894).
- [designspaceLib] Add DS.getAxisByTag and refactor getAxis (#2891).
- [unicodedata] map Zmth<->math in ot_tag_{to,from}_script (#1737, #2889).
- [woff2] Support encoding/decoding OVERLAP_SIMPLE glyf flags (#2576, #2884).
- [instancer] Update OS/2 class and post.italicAngle when default moved (L4)
- Dropped support for Python 3.7 which reached EOL, fontTools requires 3.8+.
- [instancer] Fixed instantiateFeatureVariations logic when a rule range becomes
  default-applicable (#2737, #2880).
- [ttLib] Add main to ttFont and ttCollection that just decompile and re-compile the
  input font (#2869).
- [featureVars] Insert 'rvrn' lookup at the beginning of LookupList, to work around bug
  in Apple implementation of 'rvrn' feature which the spec says it should be processed
  early whereas on macOS 10.15 it follows lookup order (#2140, #2867).
- [instancer/mutator] Remove 'DSIG' table if present.
- [svgPathPen] Don't close path in endPath(), assume open unless closePath() (#2089, #2865).

4.38.0 (released 2022-10-21)
----------------------------

- [varLib.instancer] Added support for L4 instancing, i.e. moving the default value of
  an axis while keeping it variable. Thanks Behdad! (#2728, #2861).
  It's now also possible to restrict an axis min/max values beyond the current default
  value, e.g. a font wght has min=100, def=400, max=900 and you want a partial VF that
  only varies between 500 and 700, you can now do that.
  You can either specify two min/max values (wght=500:700), and the new default will be
  set to either the minimum or maximum, depending on which one is closer to the current
  default (e.g. 500 in this case). Or you can specify three values (e.g. wght=500:600:700)
  to specify the new default value explicitly.
- [otlLib/featureVars] Set a few Count values so one doesn't need to compile the font
  to update them (#2860).
- [varLib.models] Make extrapolation work for 2-master models as well where one master
  is at the default location (#2843, #2846).
  Add optional extrapolate=False to normalizeLocation() (#2847, #2849).
- [varLib.cff] Fixed sub-optimal packing of CFF2 deltas by no longer rounding them to
  integer (#2838).
- [scaleUpem] Calculate numShorts in VarData after scale; handle CFF hintmasks (#2840).

4.37.4 (released 2022-09-30)
----------------------------

- [subset] Keep nameIDs used by CPAL palette entry labels (#2837).
- [varLib] Avoid negative hmtx values when creating font from variable CFF2 font (#2827).
- [instancer] Don't prune stat.ElidedFallbackNameID (#2828).
- [unicodedata] Update Scripts/Blocks to Unicode 15.0 (#2833).

4.37.3 (released 2022-09-20)
----------------------------

- Fix arguments in calls to (glyf) glyph.draw() and drawPoints(), whereby offset wasn't
  correctly passed down; this fix also exposed a second bug, where lsb and tsb were not
  set (#2824, #2825, adobe-type-tools/afdko#1560).

4.37.2 (released 2022-09-15)
----------------------------

- [subset] Keep CPAL table and don't attempt to prune unused color indices if OT-SVG
  table is present even if COLR table was subsetted away; OT-SVG may be referencing the
  CPAL table; for now we assume that's the case (#2814, #2815).
- [varLib.instancer] Downgrade GPOS/GSUB version if there are no more FeatureVariations
  after instancing (#2812).
- [subset] Added ``--no-lazy`` to optionally load fonts eagerly (mostly to ease
  debugging of table lazy loading, no practical effects) (#2807).
- [varLib] Avoid building empty COLR.DeltaSetIndexMap with only identity mappings (#2803).
- [feaLib] Allow multiple value record types (by promoting to the most general format)
  within the same PairPos subtable; e.g. this allows variable and non variable kerning
  rules to share the same subtable. This also fixes a bug whereby some kerning pairs
  would become unreachable while shapiong because of premature subtable splitting (#2772, #2776).
- [feaLib] Speed up ``VarScalar`` by caching models for recurring master locations (#2798).
- [feaLib] Optionally cythonize ``feaLib.lexer``, speeds up parsing FEA a bit (#2799).
- [designspaceLib] Avoid crash when handling unbounded rule conditions (#2797).
- [post] Don't crash if ``post`` legacy format 1 is malformed/improperly used (#2786)
- [gvar] Don't be "lazy" (load all glyph variations up front) when TTFont.lazy=False (#2771).
- [TTFont] Added ``normalizeLocation`` method to normalize a location dict from the
  font's defined axes space (also known as "user space") into the normalized (-1..+1)
  space. It applies ``avar`` mapping if the font contains an ``avar`` table (#2789).
- [TTVarGlyphSet] Support drawing glyph instances from CFF2 variable glyph set (#2784).
- [fontBuilder] Do not error when building cmap if there are zero code points (#2785).
- [varLib.plot] Added ability to plot a variation model and set of accompaning master
  values corresponding to the model's master locations into a pyplot figure (#2767).
- [Snippets] Added ``statShape.py`` script to draw statistical shape of a glyph as an
  ellips (requires pycairo) (baecd88).
- [TTVarGlyphSet] implement drawPoints natively, avoiding going through
  SegmentToPointPen (#2778).
- [TTVarGlyphSet] Fixed bug whereby drawing a composite glyph multiple times, its
  components would shif; needed an extra copy (#2774).

4.37.1 (released 2022-08-24)
----------------------------

- [subset] Fixed regression introduced with v4.37.0 while subsetting the VarStore of
  ``HVAR`` and ``VVAR`` tables, whereby an ``AttributeError: subset_varidxes`` was
  thrown because an apparently unused import statement (with the side-effect of
  dynamically binding that ``subset_varidxes`` method to the VarStore class) had been
  accidentally deleted in an unrelated PR (#2679, #2773).
- [pens] Added ``cairoPen`` (#2678).
- [gvar] Read ``gvar`` more lazily by not parsing all of the ``glyf`` table (#2771).
- [ttGlyphSet] Make ``drawPoints(pointPen)`` method work for CFF fonts as well via
  adapter pen (#2770).

4.37.0 (released 2022-08-23)
----------------------------

- [varLib.models] Reverted PR #2717 which added support for "narrow tents" in v4.36.0,
  as it introduced a regression (#2764, #2765). It will be restored in upcoming release
  once we found a solution to the bug.
- [cff.specializer] Fixed issue in charstring generalizer with the ``blend`` operator
  (#2750, #1975).
- [varLib.models] Added support for extrapolation (#2757).
- [ttGlyphSet] Ensure the newly added ``_TTVarGlyphSet`` inherits from ``_TTGlyphSet``
  to keep backward compatibility with existing API (#2762).
- [kern] Allow compiling legacy kern tables with more than 64k entries (d21cfdede).
- [visitor] Added new visitor API to traverse tree of objects and dispatch based
  on the attribute type: cf. ``fontTools.misc.visitor`` and ``fontTools.ttLib.ttVisitor``. Added ``fontTools.ttLib.scaleUpem`` module that uses the latter to
  change a font's units-per-em and scale all the related fields accordingly (#2718,
  #2755).

4.36.0 (released 2022-08-17)
----------------------------

- [varLib.models] Use a simpler model that generates narrower "tents" (regions, master
  supports) whenever possible: specifically when any two axes that actively "cooperate"
  (have masters at non-zero positions for both axes) have a complete set of intermediates.
  The simpler algorithm produces fewer overlapping regions and behaves better with
  respect to rounding at the peak positions than the generic solver, always matching
  intermediate masters exactly, instead of maximally 0.5 units off. This may be useful
  when 100% metrics compatibility is desired (#2218, #2717).
- [feaLib] Remove warning when about ``GDEF`` not being built when explicitly not
  requested; don't build one unconditonally even when not requested (#2744, also works
  around #2747).
- [ttFont] ``TTFont.getGlyphSet`` method now supports selecting a location that
  represents an instance of a variable font (supports both user-scale and normalized
  axes coordinates via the ``normalized=False`` parameter). Currently this only works
  for TrueType-flavored variable fonts (#2738).

4.35.0 (released 2022-08-15)
----------------------------

- [otData/otConverters] Added support for 'biased' PaintSweepGradient start/end angles
  to match latest COLRv1 spec (#2743).
- [varLib.instancer] Fixed bug in ``_instantiateFeatureVariations`` when at the same
  time pinning one axis and restricting the range of a subsequent axis; the wrong axis
  tag was being used in the latter step (as the records' axisIdx was updated in the
  preceding step but looked up using the old axes order in the following step) (#2733,
  #2734).
- [mtiLib] Pad script tags with space when less than 4 char long (#1727).
- [merge] Use ``'.'`` instead of ``'#'`` in duplicate glyph names (#2742).
- [gvar] Added support for lazily loading glyph variations (#2741).
- [varLib] In ``build_many``, we forgot to pass on ``colr_layer_reuse`` parameter to
  the ``build`` method (#2730).
- [svgPathPen] Add a main that prints SVG for input text (6df779fd).
- [cffLib.width] Fixed off-by-one in optimized values; previous code didn't match the
  code block above it (2963fa50).
- [varLib.interpolatable] Support reading .designspace and .glyphs files (via optional
  ``glyphsLib``).
- Compile some modules with Cython when available and building/installing fonttools
  from source: ``varLib.iup`` (35% faster), ``pens.momentsPen`` (makes
  ``varLib.interpolatable`` 3x faster).
- [feaLib] Allow features to be built for VF without also building a GDEF table (e.g.
  only build GSUB); warn when GDEF would be needed but isn't requested (#2705, 2694).
- [otBase] Fixed ``AttributeError`` when uharfbuzz < 0.23.0 and 'repack' method is
  missing (32aa8eaf). Use new ``uharfbuzz.repack_with_tag`` when available (since
  uharfbuzz>=0.30.0), enables table-specific optimizations to be performed during
  repacking (#2724).
- [statisticsPen] By default report all glyphs (4139d891). Avoid division-by-zero
  (52b28f90).
- [feaLib] Added missing required argument to FeatureLibError exception (#2693)
- [varLib.merge] Fixed error during error reporting (#2689). Fixed undefined
  ``NotANone`` variable (#2714).

4.34.4 (released 2022-07-07)
----------------------------

- Fixed typo in varLib/merger.py that causes NameError merging COLR glyphs
  containing more than 255 layers (#2685).

4.34.3 (released 2022-07-07)
----------------------------

- [designspaceLib] Don't make up bad PS names when no STAT data (#2684)

4.34.2 (released 2022-07-06)
----------------------------

- [varStore/subset] fixed KeyError exception to do with NO_VARIATION_INDEX while
  subsetting varidxes in GPOS/GDEF (a08140d).

4.34.1 (released 2022-07-06)
----------------------------

- [instancer] When optimizing HVAR/VVAR VarStore, use_NO_VARIATION_INDEX=False to avoid
  including NO_VARIATION_INDEX in AdvWidthMap, RsbMap, LsbMap mappings, which would
  push the VarIdx width to maximum (4bytes), which is not desirable. This also fixes
  a hard crash when attempting to subset a varfont after it had been partially instanced
  with use_NO_VARIATION_INDEX=True.

4.34.0 (released 2022-07-06)
----------------------------

- [instancer] Set RIBBI bits in head and OS/2 table when cutting instances and the
  subfamily nameID=2 contains strings like 'Italic' or 'Bold' (#2673).
- [otTraverse] Addded module containing methods for traversing trees of otData tables
  (#2660).
- [otTables] Made DeltaSetIndexMap TTX dump less verbose by omitting no-op entries
  (#2660).
- [colorLib.builder] Added option to disable PaintColrLayers's reuse of layers from
  LayerList (#2660).
- [varLib] Added support for merging multiple master COLRv1 tables into a variable
  COLR table (#2660, #2328). Base color glyphs of same name in different masters must have
  identical paint graph structure (incl. number of layers, palette indices, number
  of color line stops, corresponding paint formats at each level of the graph),
  but can differ in the variable fields (e.g. PaintSolid.Alpha). PaintVar* tables
  are produced when this happens and a VarStore/DeltaSetIndexMap is added to the
  variable COLR table. It is possible for non-default masters to be 'sparse', i.e.
  omit some of the color glyphs present in the default master.
- [feaLib] Let the Parser set nameIDs 1 through 6 that were previously reserved (#2675).
- [varLib.varStore] Support NO_VARIATION_INDEX in optimizer and instancer.
- [feaLib] Show all missing glyphs at once at end of parsing (#2665).
- [varLib.iup] Rewrite force-set conditions and limit DP loopback length (#2651).
  For Noto Sans, IUP time drops from 23s down to 9s, with only a slight size increase
  in the final font. This basically turns the algorithm from O(n^3) into O(n).
- [featureVars] Report about missing glyphs in substitution rules (#2654).
- [mutator/instancer] Added CLI flag to --no-recalc-timestamp (#2649).
- [SVG] Allow individual SVG documents in SVG OT table to be compressed on uncompressed,
  and remember that when roundtripping to/from ttx. The SVG.docList is now a list
  of SVGDocument namedtuple-like dataclass containing an extra ``compressed`` field,
  and no longer a bare 3-tuple (#2645).
- [designspaceLib] Check for descriptor types with hasattr() to allow custom classes
  that don't inherit the default descriptors (#2634).
- [subset] Enable sharing across subtables of extension lookups for harfbuzz packing
  (#2626). Updated how table packing falls back to fontTools from harfbuzz (#2668).
- [subset] Updated default feature tags following current Harfbuzz (#2637).
- [svgLib] Fixed regex for real number to support e.g. 1e-4 in addition to 1.0e-4.
  Support parsing negative rx, ry on arc commands (#2596, #2611).
- [subset] Fixed subsetting SinglePosFormat2 when ValueFormat=0 (#2603).

4.33.3 (released 2022-04-26)
----------------------------

- [designspaceLib] Fixed typo in ``deepcopyExceptFonts`` method, preventing font
  references to be transferred (#2600). Fixed another typo in the name of ``Range``
  dataclass's ``__post_init__`` magic method (#2597).

4.33.2 (released 2022-04-22)
----------------------------

- [otBase] Make logging less verbose when harfbuzz fails to serialize. Do not exit
  at the first failure but continue attempting to fix offset overflow error using
  the pure-python serializer even when the ``USE_HARFBUZZ_REPACKER`` option was
  explicitly set to ``True``. This is normal with fonts with relatively large
  tables, at least until hb.repack implements proper table splitting.

4.33.1 (released 2022-04-22)
----------------------------

- [otlLib] Put back the ``FONTTOOLS_GPOS_COMPACT_MODE`` environment variable to fix
  regression in ufo2ft (and thus fontmake) introduced with v4.33.0 (#2592, #2593).
  This is deprecated and will be removed one ufo2ft gets updated to use the new
  config setup.

4.33.0 (released 2022-04-21)
----------------------------

- [OS/2 / merge] Automatically recalculate ``OS/2.xAvgCharWidth`` after merging
  fonts with ``fontTools.merge`` (#2591, #2538).
- [misc/config] Added ``fontTools.misc.configTools`` module, a generic configuration
  system (#2416, #2439).
  Added ``fontTools.config`` module, a fontTools-specific configuration
  system using ``configTools`` above.
  Attached a ``Config`` object to ``TTFont``.
- [otlLib] Replaced environment variable for GPOS compression level with an
  equivalent option using the new config system.
- [designspaceLib] Incremented format version to 5.0 (#2436).
  Added discrete axes, variable fonts, STAT information, either design- or
  user-space location on instances.
  Added ``fontTools.designspaceLib.split`` module to split a designspace
  into sub-spaces that interpolate and that represent the variable fonts
  listed in the document.
  Made instance names optional and allow computing them from STAT data instead.
  Added ``fontTools.designspaceLib.statNames`` module.
  Allow instances to have the same location as a previously defined STAT label.
  Deprecated some attributes:
  ``SourceDescriptor``: ``copyLib``, ``copyInfo``, ``copyGroups``, ``copyFeatures``.
  ``InstanceDescriptor``: ``kerning``, ``info``; ``glyphs``: use rules or sparse
  sources.
  For both, ``location``: use the more explicit designLocation.
  Note: all are soft deprecations and existing code should keep working.
  Updated documentation for Python methods and the XML format.
- [varLib] Added ``build_many`` to build several variable fonts from a single
  designspace document (#2436).
  Added ``fontTools.varLib.stat`` module to build STAT tables from a designspace
  document.
- [otBase] Try to use the Harfbuzz Repacker for packing GSUB/GPOS tables when
  ``uharfbuzz`` python bindings are available (#2552). Disable it by setting the
  "fontTools.ttLib.tables.otBase:USE_HARFBUZZ_REPACKER" config option to ``False``.
  If the option is set explicitly to ``True`` but ``uharfbuzz`` can't be imported
  or fails to serialize for any reasons, an error will be raised (ImportError or
  uharfbuzz errors).
- [CFF/T2] Ensure that ``pen.closePath()`` gets called for CFF2 charstrings (#2577).
  Handle implicit CFF2 closePath within ``T2OutlineExtractor`` (#2580).

4.32.0 (released 2022-04-08)
----------------------------

- [otlLib] Disable GPOS7 optimization to work around bug in Apple CoreText.
  Always force Chaining GPOS8 for now (#2540).
- [glifLib] Added ``outputImpliedClosingLine=False`` parameter to ``Glyph.draw()``,
  to control behaviour of ``PointToSegmentPen`` (6b4e2e7).
- [varLib.interpolatable] Check for wrong contour starting point (#2571).
- [cffLib] Remove leftover ``GlobalState`` class and fix calls to ``TopDictIndex()``
  (#2569, #2570).
- [instancer] Clear ``AxisValueArray`` if it is empty after instantiating (#2563).

4.31.2 (released 2022-03-22)
----------------------------

- [varLib] fix instantiation of GPOS SinglePos values (#2555).

4.31.1 (released 2022-03-18)
----------------------------

- [subset] fix subsetting OT-SVG when glyph id attribute is on the root ``<svg>``
  element (#2553).

4.31.0 (released 2022-03-18)
----------------------------

- [ttCollection] Fixed 'ResourceWarning: unclosed file' warning (#2549).
- [varLib.merger] Handle merging SinglePos with valueformat=0 (#2550).
- [ttFont] Update glyf's glyphOrder when calling TTFont.setGlyphOrder() (#2544).
- [ttFont] Added ``ensureDecompiled`` method to load all tables irrespective
  of the ``lazy`` attribute (#2551).
- [otBase] Added ``iterSubTable`` method to iterate over BaseTable's children of
  type BaseTable; useful for traversing a tree of otTables (#2551).

4.30.0 (released 2022-03-10)
----------------------------

- [varLib] Added debug logger showing the glyph name for which ``gvar`` is built (#2542).
- [varLib.errors] Fixed undefined names in ``FoundANone`` and ``UnsupportedFormat``
  exceptions (ac4d5611).
- [otlLib.builder] Added ``windowsNames`` and ``macNames`` (bool) parameters to the
  ``buildStatTabe`` function, so that one can select whether to only add one or both
  of the two sets (#2528).
- [t1Lib] Added the ability to recreate PostScript stream (#2504).
- [name] Added ``getFirstDebugName``, ``getBest{Family,SubFamily,Full}Name`` methods (#2526).

4.29.1 (released 2022-02-01)
----------------------------

- [colorLib] Fixed rounding issue with radial gradient's start/end circles inside
  one another (#2521).
- [freetypePen] Handle rotate/skew transform when auto-computing width/height of the
  buffer; raise PenError wen missing moveTo (#2517)

4.29.0 (released 2022-01-24)
----------------------------

- [ufoLib] Fixed illegal characters and expanded reserved filenames (#2506).
- [COLRv1] Don't emit useless PaintColrLayers of lenght=1 in LayerListBuilder (#2513).
- [ttx] Removed legacy ``waitForKeyPress`` method on Windows (#2509).
- [pens] Added FreeTypePen that uses ``freetype-py`` and the pen protocol for
  rasterizating outline paths (#2494).
- [unicodedata] Updated the script direction list to Unicode 14.0 (#2484).
  Bumped unicodedata2 dependency to 14.0 (#2499).
- [psLib] Fixed type of ``fontName`` in ``suckfont`` (#2496).

4.28.5 (released 2021-12-19)
----------------------------

- [svgPathPen] Continuation of #2471: make sure all occurrences of ``str()`` are now
  replaced with user-defined ``ntos`` callable.
- [merge] Refactored code into submodules, plus several bugfixes and improvements:
  fixed duplicate-glyph-resolution GSUB-lookup generation code; use tolerance in glyph
  comparison for empty glyph's width; ignore space of default ignorable glyphs;
  downgrade duplicates-resolution missing-GSUB from assert to warn; added --drop-tables
  option (#2473, #2475, #2476).

4.28.4 (released 2021-12-15)
----------------------------

- [merge] Merge GDEF marksets in Lookups properly (#2474).
- [feaLib] Have ``fontTools feaLib`` script exit with error code when build fails (#2459)
- [svgPathPen] Added ``ntos`` option to customize number formatting (e.g. rounding) (#2471).
- [subset] Speed up subsetting of large CFF fonts (#2467).
- [otTables] Speculatively promote lookups to extension to speed up compilation. If the
  offset to lookup N is too big to fit in a ushort, the offset to lookup N+1 is going to
  be too big as well, so we promote to extension all lookups from lookup N onwards (#2465).

4.28.3 (released 2021-12-03)
----------------------------

- [subset] Fixed bug while subsetting ``COLR`` table, whereby incomplete layer records
  pointing to missing glyphs were being retained leading to ``struct.error`` upon
  compiling. Make it so that ``glyf`` glyph closure, which follows the ``COLR`` glyph
  closure, does not influence the ``COLR`` table subsetting (#2461, #2462).
- [docs] Fully document the ``cmap`` and ``glyf`` tables (#2454, #2457).
- [colorLib.unbuilder] Fixed CLI by deleting no longer existing parameter (180bb1867).

4.28.2 (released 2021-11-22)
----------------------------

- [otlLib] Remove duplicates when building coverage (#2433).
- [docs] Add interrogate configuration (#2443).
- [docs] Remove comment about missing “start” optional argument to ``calcChecksum`` (#2448).
- [cu2qu/cli] Adapt to the latest ufoLib2.
- [subset] Support subsetting SVG table and remove it from the list of  drop by default tables (#534).
- [subset] add ``--pretty-svg`` option to pretty print SVG table contents (#2452).
- [merge] Support merging ``CFF`` tables (CID-keyed ``CFF`` is still not supported) (#2447).
- [merge] Support ``--output-file`` (#2447).
- [docs] Split table docs into individual pages (#2444).
- [feaLib] Forbid empty classes (#2446).
- [docs] Improve documentation for ``fontTools.ttLib.ttFont`` (#2442).

4.28.1 (released 2021-11-08)
----------------------------

- [subset] Fixed AttributeError while traversing a color glyph's Paint graph when there is no
  LayerList, which is optional (#2441).

4.28.0 (released 2021-11-05)
----------------------------

- Dropped support for EOL Python 3.6, require Python 3.7 (#2417).
- [ufoLib/glifLib] Make filename-clash checks faster by using a set instead of a list (#2422).
- [subset] Don't crash if optional ClipList and LayerList are ``None`` (empty) (#2424, 2439).
- [OT-SVG] Removed support for old deprecated version 1 and embedded color palettes,
  which were never officially part of the OpenType SVG spec. Upon compile, reuse offsets
  to SVG documents that are identical (#2430).
- [feaLib] Added support for Variable Feature File syntax. This is experimental and subject
  to change until it is finalized in the Adobe FEA spec (#2432).
- [unicodedata] Update Scripts/ScriptExtensions/Blocks to UnicodeData 14.0 (#2437).

4.27.1 (released 2021-09-23)
----------------------------

- [otlLib] Fixed error when chained contextual lookup builder overflows (#2404, #2411).
- [bezierTools] Fixed two floating-point bugs: one when computing `t` for a point
  lying on an almost horizontal/vertical line; another when computing the intersection
  point between a curve and a line (#2413).

4.27.0 (released 2021-09-14)
----------------------------

- [ttLib/otTables] Cleaned up virtual GID handling: allow virtual GIDs in ``Coverage``
  and ``ClassDef`` readers; removed unused ``allowVID`` argument from ``TTFont``
  constructor, and ``requireReal`` argument in ``TTFont.getGlyphID`` method.
  Make ``TTFont.setGlyphOrder`` clear reverse glyphOrder map, and assume ``glyphOrder``
  internal attribute is never modified outside setGlyphOrder; added ``TTFont.getGlyphNameMany``
  and ``getGlyphIDMany`` (#1536, #1654, #2334, #2398).
- [py23] Dropped internal use of ``fontTools.py23`` module to fix deprecation warnings
  in client code that imports from fontTools (#2234, #2399, #2400).
- [subset] Fix subsetting COLRv1 clip boxes when font is loaded lazily (#2408).

4.26.2 (released 2021-08-09)
----------------------------

- [otTables] Added missing ``CompositeMode.PLUS`` operator (#2390).

4.26.1 (released 2021-08-03)
----------------------------

- [transform] Added ``transformVector`` and ``transformVectors`` methods to the
  ``Transform`` class. Similar to ``transformPoint`` but ignore the translation
  part (#2386).

4.26.0 (released 2021-08-03)
----------------------------

- [xmlWriter] Default to ``"\n"`` for ``newlinestr`` instead of platform-specific
  ``os.linesep`` (#2384).
- [otData] Define COLRv1 ClipList and ClipBox (#2379).
- [removeOverlaps/instancer] Added --ignore-overlap-errors option to work around
  Skia PathOps.Simplify bug (#2382, #2363, google/fonts#3365).
- NOTE: This will be the last version to support Python 3.6. FontTools will require
  Python 3.7 or above from the next release (#2350)

4.25.2 (released 2021-07-26)
----------------------------

- [COLRv1] Various changes to sync with the latest CORLv1 draft spec. In particular:
  define COLR.VarIndexMap, remove/inline ColorIndex struct, add VarIndexBase to ``PaintVar*`` tables (#2372);
  add reduced-precicion specialized transform Paints;
  define Angle as fraction of half circle encoded as F2Dot14;
  use FWORD (int16) for all Paint center coordinates;
  change PaintTransform to have an offset to Affine2x3;
- [ttLib] when importing XML, only set sfntVersion if the font has no reader and is empty (#2376)

4.25.1 (released 2021-07-16)
----------------------------

- [ttGlyphPen] Fixed bug in ``TTGlyphPointPen``, whereby open contours (i.e. starting
  with segmentType "move") would throw ``NotImplementedError``. They are now treated
  as if they are closed, like with the ``TTGlyphPen`` (#2364, #2366).

4.25.0 (released 2021-07-05)
----------------------------

- [tfmLib] Added new library for parsing TeX Font Metric (TFM) files (#2354).
- [TupleVariation] Make shared tuples order deterministic on python < 3.7 where
  Counter (subclass of dict) doesn't remember insertion order (#2351, #2353).
- [otData] Renamed COLRv1 structs to remove 'v1' suffix and match the updated draft
  spec: 'LayerV1List' -> 'LayerList', 'BaseGlyphV1List' -> 'BaseGlyphList',
  'BaseGlyphV1Record' -> 'BaseGlyphPaintRecord' (#2346).
  Added 8 new ``PaintScale*`` tables: with/without centers, uniform vs non-uniform.
  Added ``*AroundCenter`` variants to ``PaintRotate`` and ``PaintSkew``: the default
  versions no longer have centerX/Y, but default to origin.
  ``PaintRotate``, ``PaintSkew`` and ``PaintComposite`` formats were re-numbered.
  NOTE: these are breaking changes; clients using the experimental COLRv1 API will
  have to be updated (#2348).
- [pointPens] Allow ``GuessSmoothPointPen`` to accept a tolerance. Fixed call to
  ``math.atan2`` with x/y parameters inverted. Sync the code with fontPens (#2344).
- [post] Fixed parsing ``post`` table format 2.0 when it contains extra garbage
  at the end of the stringData array (#2314).
- [subset] drop empty features unless 'size' with FeatureParams table (#2324).
- [otlLib] Added ``otlLib.optimize`` module; added GPOS compaction algorithm.
  The compaction can be run on existing fonts with ``fonttools otlLib.optimize``
  or using the snippet ``compact_gpos.py``. There's experimental support for
  compacting fonts at compilation time using an environment variable, but that
  might be removed later (#2326).

4.24.4 (released 2021-05-25)
----------------------------

- [subset/instancer] Fixed ``AttributeError`` when instantiating a VF that
  contains GPOS ValueRecords with ``Device`` tables but without the respective
  non-Device values (e.g. ``XAdvDevice`` without ``XAdvance``). When not
  explicitly set, the latter are assumed to be 0 (#2323).

4.24.3 (released 2021-05-20)
----------------------------

- [otTables] Fixed ``AttributeError`` in methods that split LigatureSubst,
  MultipleSubst and AlternateSubst subtables when an offset overflow occurs.
  The ``Format`` attribute was removed in v4.22.0 (#2319).

4.24.2 (released 2021-05-20)
----------------------------

- [ttGlyphPen] Fixed typing annotation of TTGlyphPen glyphSet parameter (#2315).
- Fixed two instances of DeprecationWarning: invalid escape sequence (#2311).

4.24.1 (released 2021-05-20)
----------------------------

- [subset] Fixed AttributeError when SinglePos subtable has None Value (ValueFormat 0)
  (#2312, #2313).

4.24.0 (released 2021-05-17)
----------------------------

- [pens] Add ``ttGlyphPen.TTGlyphPointPen`` similar to ``TTGlyphPen`` (#2205).

4.23.1 (released 2021-05-14)
----------------------------

- [subset] Fix ``KeyError`` after subsetting ``COLR`` table that initially contains
  both v0 and v1 color glyphs when the subset only requested v1 glyphs; we were
  not pruning the v0 portion of the table (#2308).
- [colorLib] Set ``LayerV1List`` attribute to ``None`` when empty, it's optional
  in CORLv1 (#2308).

4.23.0 (released 2021-05-13)
----------------------------

- [designspaceLib] Allow to use ``\\UNC`` absolute paths on Windows (#2299, #2306).
- [varLib.merger] Fixed bug where ``VarLibMergeError`` was raised with incorrect
  parameters (#2300).
- [feaLib] Allow substituting a glyph class with ``NULL`` to delete multiple glyphs
  (#2303).
- [glyf] Fixed ``NameError`` exception in ``getPhantomPoints`` (#2295, #2305).
- [removeOverlaps] Retry pathops.simplify after rounding path coordinates to integers
  if it fails the first time using floats, to work around a rare and hard to debug
  Skia bug (#2288).
- [varLib] Added support for building, reading, writing and optimizing 32-bit
  ``ItemVariationStore`` as used in COLRv1 table (#2285).
- [otBase/otConverters] Add array readers/writers for int types (#2285).
- [feaLib] Allow more than one lookahead glyph/class in contextual positioning with
  "value at end" (#2293, #2294).
- [COLRv1] Default varIdx should be 0xFFFFFFFF (#2297, #2298).
- [pens] Make RecordingPointPen actually pass on identifiers; replace asserts with
  explicit ``PenError`` exception (#2284).
- [mutator] Round lsb for CF2 fonts as well (#2286).

4.22.1 (released 2021-04-26)
----------------------------

- [feaLib] Skip references to named lookups if the lookup block definition
  is empty, similarly to makeotf. This also fixes an ``AttributeError`` while
  generating ``aalt`` feature (#2276, #2277).
- [subset] Fixed bug with ``--no-hinting`` implementation for Device tables (#2272,
  #2275). The previous code was alwyas dropping Device tables if no-hinting was
  requested, but some Device tables (DeltaFormat=0x8000) are also used to encode
  variation indices and need to be retained.
- [otBase] Fixed bug in getting the ValueRecordSize when decompiling ``MVAR``
  table with ``lazy=True`` (#2273, #2274).
- [varLib/glyf/gvar] Optimized and simplified ``GlyphCoordinates`` and
  ``TupleVariation`` classes, use ``bytearray`` where possible, refactored
  phantom-points calculations. We measured about 30% speedup in total time
  of loading master ttfs, building gvar, and saving (#2261, #2266).
- [subset] Fixed ``AssertionError`` while pruning unused CPAL palettes when
  ``0xFFFF`` is present (#2257, #2259).

4.22.0 (released 2021-04-01)
----------------------------

- [ttLib] Remove .Format from Coverage, ClassDef, SingleSubst, LigatureSubst,
  AlternateSubst, MultipleSubst (#2238).
  ATTENTION: This will change your TTX dumps!
- [misc.arrayTools] move Vector to its own submodule, and rewrite as a tuple
  subclass (#2201).
- [docs] Added a terminology section for varLib (#2209).
- [varLib] Move rounding to VariationModel, to avoid error accumulation from
  multiple deltas (#2214)
- [varLib] Explain merge errors in more human-friendly terms (#2223, #2226)
- [otlLib] Correct some documentation (#2225)
- [varLib/otlLib] Allow merging into VariationFont without first saving GPOS
  PairPos2 (#2229)
- [subset] Improve PairPosFormat2 subsetting (#2221)
- [ttLib] TTFont.save: create file on disk as late as possible (#2253)
- [cffLib] Add missing CFF2 dict operators LanguageGroup and ExpansionFactor
  (#2249)
  ATTENTION: This will change your TTX dumps!

4.21.1 (released 2021-02-26)
----------------------------

- [pens] Reverted breaking change that turned ``AbstractPen`` and ``AbstractPointPen``
  into abstract base classes (#2164, #2198).

4.21.0 (released 2021-02-26)
----------------------------

- [feaLib] Indent anchor statements in ``asFea()`` to make them more legible and
  diff-able (#2193).
- [pens] Turn ``AbstractPen`` and ``AbstractPointPen`` into abstract base classes
  (#2164).
- [feaLib] Added support for parsing and building ``STAT`` table from AFDKO feature
  files (#2039).
- [instancer] Added option to update name table of generated instance using ``STAT``
  table's axis values (#2189).
- [bezierTools] Added functions to compute bezier point-at-time, as well as line-line,
  curve-line and curve-curve intersections (#2192).

4.20.0 (released 2021-02-15)
----------------------------

- [COLRv1] Added ``unbuildColrV1`` to deconstruct COLRv1 otTables to raw json-able
  data structure; it does the reverse of ``buildColrV1`` (#2171).
- [feaLib] Allow ``sub X by NULL`` sequence to delete a glyph (#2170).
- [arrayTools] Fixed ``Vector`` division (#2173).
- [COLRv1] Define new ``PaintSweepGradient`` (#2172).
- [otTables] Moved ``Paint.Format`` enum class outside of ``Paint`` class definition,
  now named ``PaintFormat``. It was clashing with paint instance ``Format`` attribute
  and thus was breaking lazy load of COLR table which relies on magic ``__getattr__``
  (#2175).
- [COLRv1] Replace hand-coded builder functions with otData-driven dynamic
  implementation (#2181).
- [COLRv1] Define additional static (non-variable) Paint formats (#2181).
- [subset] Added support for subsetting COLR v1 and CPAL tables (#2174, #2177).
- [fontBuilder] Allow ``setupFvar`` to optionally take ``designspaceLib.AxisDescriptor``
  objects. Added new ``setupAvar`` method. Support localised names for axes and
  named instances (#2185).

4.19.1 (released 2021-01-28)
----------------------------

- [woff2] An initial off-curve point with an overlap flag now stays an off-curve
  point after compression.

4.19.0 (released 2021-01-25)
----------------------------

- [codecs] Handle ``errors`` parameter different from 'strict' for the custom
  extended mac encodings (#2137, #2132).
- [featureVars] Raise better error message when a script is missing the required
  default language system (#2154).
- [COLRv1] Avoid abrupt change caused by rounding ``PaintRadialGradient.c0`` when
  the start circle almost touches the end circle's perimeter (#2148).
- [COLRv1] Support building unlimited lists of paints as 255-ary trees of
  ``PaintColrLayers`` tables (#2153).
- [subset] Prune redundant format-12 cmap subtables when all non-BMP characters
  are dropped (#2146).
- [basePen] Raise ``MissingComponentError`` instead of bare ``KeyError`` when a
  referenced component is missing (#2145).

4.18.2 (released 2020-12-16)
----------------------------

- [COLRv1] Implemented ``PaintTranslate`` paint format (#2129).
- [varLib.cff] Fixed unbound local variable error (#1787).
- [otlLib] Don't crash when creating OpenType class definitions if some glyphs
  occur more than once (#2125).

4.18.1 (released 2020-12-09)
----------------------------

- [colorLib] Speed optimization for ``LayerV1ListBuilder`` (#2119).
- [mutator] Fixed missing tab in ``interpolate_cff2_metrics`` (0957dc7a).

4.18.0 (released 2020-12-04)
----------------------------

- [COLRv1] Update to latest draft: added ``PaintRotate`` and ``PaintSkew`` (#2118).
- [woff2] Support new ``brotlicffi`` bindings for PyPy (#2117).
- [glifLib] Added ``expectContentsFile`` parameter to ``GlyphSet``, for use when
  reading existing UFOs, to comply with the specification stating that a
  ``contents.plist`` file must exist in a glyph set (#2114).
- [subset] Allow ``LangSys`` tags in ``--layout-scripts`` option (#2112). For example:
  ``--layout-scripts=arab.dflt,arab.URD,latn``; this will keep ``DefaultLangSys``
  and ``URD`` language for ``arab`` script, and all languages for ``latn`` script.
- [varLib.interpolatable] Allow UFOs to be checked; report open paths, non existant
  glyphs; add a ``--json`` option to produce a machine-readable list of
  incompatibilities
- [pens] Added ``QuartzPen`` to create ``CGPath`` from glyph outlines on macOS.
  Requires pyobjc (#2107).
- [feaLib] You can export ``FONTTOOLS_LOOKUP_DEBUGGING=1`` to enable feature file
  debugging info stored in ``Debg`` table (#2106).
- [otlLib] Build more efficient format 1 and format 2 contextual lookups whenever
  possible (#2101).

4.17.1 (released 2020-11-16)
----------------------------

- [colorLib] Fixed regression in 4.17.0 when building COLR v0 table; when color
  layers are stored in UFO lib plist, we can't distinguish tuples from lists so
  we need to accept either types (e5439eb9, googlefonts/ufo2ft/issues#426).

4.17.0 (released 2020-11-12)
----------------------------

- [colorLib/otData] Updated to latest draft ``COLR`` v1 spec (#2092).
- [svgLib] Fixed parsing error when arc commands' boolean flags are not separated
  by space or comma (#2094).
- [varLib] Interpret empty non-default glyphs as 'missing', if the default glyph is
  not empty (#2082).
- [feaLib.builder] Only stash lookup location for ``Debg`` if ``Builder.buildLookups_``
  has cooperated (#2065, #2067).
- [varLib] Fixed bug in VarStore optimizer (#2073, #2083).
- [varLib] Add designspace lib key for custom feavar feature tag (#2080).
- Add HashPointPen adapted from psautohint. With this pen, a hash value of a glyph
  can be computed, which can later be used to detect glyph changes (#2005).

4.16.1 (released 2020-10-05)
----------------------------

- [varLib.instancer] Fixed ``TypeError`` exception when instantiating a VF with
  a GSUB table 1.1 in which ``FeatureVariations`` attribute is present but set to
  ``None`` -- indicating that optional ``FeatureVariations`` is missing (#2077).
- [glifLib] Make ``x`` and ``y`` attributes of the ``point`` element required
  even when validation is turned off, and raise a meaningful ``GlifLibError``
  message when that happens (#2075).

4.16.0 (released 2020-09-30)
----------------------------

- [removeOverlaps] Added new module and ``removeOverlaps`` function that merges
  overlapping contours and components in TrueType glyphs. It requires the
  `skia-pathops <https://github.com/fonttools/skia-pathops>`__ module.
  Note that removing overlaps invalidates the TrueType hinting (#2068).
- [varLib.instancer] Added ``--remove-overlaps`` command-line option.
  The ``overlap`` option in ``instantiateVariableFont`` now takes an ``OverlapMode``
  enum: 0: KEEP_AND_DONT_SET_FLAGS, 1: KEEP_AND_SET_FLAGS (default), and 2: REMOVE.
  The latter is equivalent to calling ``removeOverlaps`` on the generated static
  instance. The option continues to accept ``bool`` value for backward compatibility.


4.15.0 (released 2020-09-21)
----------------------------

- [plistlib] Added typing annotations to plistlib module. Set up mypy static
  typechecker to run automatically on CI (#2061).
- [ttLib] Implement private ``Debg`` table, a reverse-DNS namespaced JSON dict.
- [feaLib] Optionally add an entry into the ``Debg`` table with the original
  lookup name (if any), feature name / script / language combination (if any),
  and original source filename and line location. Annotate the ttx output for
  a lookup with the information from the Debg table (#2052).
- [sfnt] Disabled checksum checking by default in ``SFNTReader`` (#2058).
- [Docs] Document ``mtiLib`` module (#2027).
- [varLib.interpolatable] Added checks for contour node count and operation type
  of each node (#2054).
- [ttLib] Added API to register custom table packer/unpacker classes (#2055).

4.14.0 (released 2020-08-19)
----------------------------

- [feaLib] Allow anonymous classes in LookupFlags definitions (#2037).
- [Docs] Better document DesignSpace rules processing order (#2041).
- [ttLib] Fixed 21-year old bug in ``maxp.maxComponentDepth`` calculation (#2044,
  #2045).
- [varLib.models] Fixed misspelled argument name in CLI entry point (81d0042a).
- [subset] When subsetting GSUB v1.1, fixed TypeError by checking whether the
  optional FeatureVariations table is present (e63ecc5b).
- [Snippets] Added snippet to show how to decompose glyphs in a TTF (#2030).
- [otlLib] Generate GSUB type 5 and GPOS type 7 contextual lookups where appropriate
  (#2016).

4.13.0 (released 2020-07-10)
----------------------------

- [feaLib/otlLib] Moved lookup subtable builders from feaLib to otlLib; refactored
  some common code (#2004, #2007).
- [docs] Document otlLib module (#2009).
- [glifLib] Fixed bug with some UFO .glif filenames clashing on case-insensitive
  filesystems (#2001, #2002).
- [colorLib] Updated COLRv1 implementation following changes in the draft spec:
  (#2008, googlefonts/colr-gradients-spec#24).

4.12.1 (released 2020-06-16)
----------------------------

- [_n_a_m_e] Fixed error in ``addMultilingualName`` with one-character names.
  Only attempt to recovered malformed UTF-16 data from a ``bytes`` string,
  not from unicode ``str`` (#1997, #1998).

4.12.0 (released 2020-06-09)
----------------------------

- [otlLib/varLib] Ensure that the ``AxisNameID`` in the ``STAT`` and ``fvar``
  tables is grater than 255 as per OpenType spec (#1985, #1986).
- [docs] Document more modules in ``fontTools.misc`` package: ``filenames``,
  ``fixedTools``, ``intTools``, ``loggingTools``, ``macCreatorType``, ``macRes``,
  ``plistlib`` (#1981).
- [OS/2] Don't calculate whole sets of unicode codepoints, use faster and more memory
  efficient ranges and bisect lookups (#1984).
- [voltLib] Support writing back abstract syntax tree as VOLT data (#1983).
- [voltLib] Accept DO_NOT_TOUCH_CMAP keyword (#1987).
- [subset/merge] Fixed a namespace clash involving a private helper class (#1955).

4.11.0 (released 2020-05-28)
----------------------------

- [feaLib] Introduced ``includeDir`` parameter on Parser and IncludingLexer to
  explicitly specify the directory to search when ``include()`` statements are
  encountered (#1973).
- [ufoLib] Silently delete duplicate glyphs within the same kerning group when reading
  groups (#1970).
- [ttLib] Set version of COLR table when decompiling COLRv1 (commit 9d8a7e2).

4.10.2 (released 2020-05-20)
----------------------------

- [sfnt] Fixed ``NameError: SimpleNamespace`` while reading TTC header. The regression
  was introduced with 4.10.1 after removing ``py23`` star import.

4.10.1 (released 2020-05-19)
----------------------------

- [sfnt] Make ``SFNTReader`` pickleable even when TTFont is loaded with lazy=True
  option and thus keeps a reference to an external file (#1962, #1967).
- [feaLib.ast] Restore backward compatibility (broken in 4.10 with #1905) for
  ``ChainContextPosStatement`` and ``ChainContextSubstStatement`` classes.
  Make them accept either list of lookups or list of lists of lookups (#1961).
- [docs] Document some modules in ``fontTools.misc`` package: ``arrayTools``,
  ``bezierTools`` ``cliTools`` and ``eexec`` (#1956).
- [ttLib._n_a_m_e] Fixed ``findMultilingualName()`` when name record's ``string`` is
  encoded as bytes sequence (#1963).

4.10.0 (released 2020-05-15)
----------------------------

- [varLib] Allow feature variations to be active across the entire space (#1957).
- [ufoLib] Added support for ``formatVersionMinor`` in UFO's ``fontinfo.plist`` and for
  ``formatMinor`` attribute in GLIF file as discussed in unified-font-object/ufo-spec#78.
  No changes in reading or writing UFOs until an upcoming (non-0) minor update of the
  UFO specification is published (#1786).
- [merge] Fixed merging fonts with different versions of ``OS/2`` table (#1865, #1952).
- [subset] Fixed ``AttributeError`` while subsetting ``ContextSubst`` and ``ContextPos``
  Format 3 subtable (#1879, #1944).
- [ttLib.table._m_e_t_a] if data happens to be ascii, emit comment in TTX (#1938).
- [feaLib] Support multiple lookups per glyph position (#1905).
- [psCharStrings] Use inheritance to avoid repeated code in initializer (#1932).
- [Doc] Improved documentation for the following modules: ``afmLib`` (#1933), ``agl``
  (#1934), ``cffLib`` (#1935), ``cu2qu`` (#1937), ``encodings`` (#1940), ``feaLib``
  (#1941), ``merge`` (#1949).
- [Doc] Split off developer-centric info to new page, making front page of docs more
  user-focused. List all utilities and sub-modules with brief descriptions.
  Make README more concise and focused (#1914).
- [otlLib] Add function to build STAT table from high-level description (#1926).
- [ttLib._n_a_m_e] Add ``findMultilingualName()`` method (#1921).
- [unicodedata] Update ``RTL_SCRIPTS`` for Unicode 13.0 (#1925).
- [gvar] Sort ``gvar`` XML output by glyph name, not glyph order (#1907, #1908).
- [Doc] Added help options to ``fonttools`` command line tool (#1913, #1920).
  Ensure all fonttools CLI tools have help documentation (#1948).
- [ufoLib] Only write fontinfo.plist when there actually is content (#1911).

4.9.0 (released 2020-04-29)
---------------------------

- [subset] Fixed subsetting of FeatureVariations table. The subsetter no longer drops
  FeatureVariationRecords that have empty substitutions as that will keep the search
  going and thus change the logic. It will only drop empty records that occur at the
  end of the FeatureVariationRecords array (#1881).
- [subset] Remove FeatureVariations table and downgrade GSUB/GPOS to version 0x10000
  when FeatureVariations contain no FeatureVariationRecords after subsetting (#1903).
- [agl] Add support for legacy Adobe Glyph List of glyph names in ``fontTools.agl``
  (#1895).
- [feaLib] Ignore superfluous script statements (#1883).
- [feaLib] Hide traceback by default on ``fonttools feaLib`` command line.
  Use ``--traceback`` option to show (#1898).
- [feaLib] Check lookup index in chaining sub/pos lookups and print better error
  message (#1896, #1897).
- [feaLib] Fix building chained alt substitutions (#1902).
- [Doc] Included all fontTools modules in the sphinx-generated documentation, and
  published it to ReadTheDocs for continuous documentation of the fontTools project
  (#1333). Check it out at https://fonttools.readthedocs.io/. Thanks to Chris Simpkins!
- [transform] The ``Transform`` class is now subclass of ``typing.NamedTuple``. No
  change in functionality (#1904).


4.8.1 (released 2020-04-17)
---------------------------

- [feaLib] Fixed ``AttributeError: 'NoneType' has no attribute 'getAlternateGlyphs'``
  when ``aalt`` feature references a chain contextual substitution lookup
  (googlefonts/fontmake#648, #1878).

4.8.0 (released 2020-04-16)
---------------------------

- [feaLib] If Parser is initialized without a ``glyphNames`` parameter, it cannot
  distinguish between a glyph name containing an hyphen, or a range of glyph names;
  instead of raising an error, it now interprets them as literal glyph names, while
  also outputting a logging warning to alert user about the ambiguity (#1768, #1870).
- [feaLib] When serializing AST to string, emit spaces around hyphens that denote
  ranges. Also, fixed an issue with CID ranges when round-tripping AST->string->AST
  (#1872).
- [Snippets/otf2ttf] In otf2ttf.py script update LSB in hmtx to match xMin (#1873).
- [colorLib] Added experimental support for building ``COLR`` v1 tables as per
  the `colr-gradients-spec <https://github.com/googlefonts/colr-gradients-spec/blob/main/colr-gradients-spec.md>`__
  draft proposal. **NOTE**: both the API and the XML dump of ``COLR`` v1 are
  susceptible to change while the proposal is being discussed and formalized (#1822).

4.7.0 (released 2020-04-03)
---------------------------

- [cu2qu] Added ``fontTools.cu2qu`` package, imported from the original
  `cu2qu <https://github.com/googlefonts/cu2qu>`__ project. The ``cu2qu.pens`` module
  was moved to ``fontTools.pens.cu2quPen``. The optional cu2qu extension module
  can be compiled by installing `Cython <https://cython.org/>`__ before installing
  fonttools from source (i.e. git repo or sdist tarball). The wheel package that
  is published on PyPI (i.e. the one ``pip`` downloads, unless ``--no-binary``
  option is used), will continue to be pure-Python for now (#1868).

4.6.0 (released 2020-03-24)
---------------------------

- [varLib] Added support for building variable ``BASE`` table version 1.1 (#1858).
- [CPAL] Added ``fromRGBA`` method to ``Color`` class (#1861).


4.5.0 (released 2020-03-20)
---------------------------

- [designspaceLib] Added ``add{Axis,Source,Instance,Rule}Descriptor`` methods to
  ``DesignSpaceDocument`` class, to initialize new descriptor objects using keyword
  arguments, and at the same time append them to the current document (#1860).
- [unicodedata] Update to Unicode 13.0 (#1859).

4.4.3 (released 2020-03-13)
---------------------------

- [varLib] Always build ``gvar`` table for TrueType-flavored Variable Fonts,
  even if it contains no variation data. The table is required according to
  the OpenType spec (#1855, #1857).

4.4.2 (released 2020-03-12)
---------------------------

- [ttx] Annotate ``LookupFlag`` in XML dump with comment explaining what bits
  are set and what they mean (#1850).
- [feaLib] Added more descriptive message to ``IncludedFeaNotFound`` error (#1842).

4.4.1 (released 2020-02-26)
---------------------------

- [woff2] Skip normalizing ``glyf`` and ``loca`` tables if these are missing from
  a font (e.g. in NotoColorEmoji using ``CBDT/CBLC`` tables).
- [timeTools] Use non-localized date parsing in ``timestampFromString``, to fix
  error when non-English ``LC_TIME`` locale is set (#1838, #1839).
- [fontBuilder] Make sure the CFF table generated by fontBuilder can be used by varLib
  without having to compile and decompile the table first. This was breaking in
  converting the CFF table to CFF2 due to some unset attributes (#1836).

4.4.0 (released 2020-02-18)
---------------------------

- [colorLib] Added ``fontTools.colorLib.builder`` module, initially with ``buildCOLR``
  and ``buildCPAL`` public functions. More color font formats will follow (#1827).
- [fontBuilder] Added ``setupCOLR`` and ``setupCPAL`` methods (#1826).
- [ttGlyphPen] Quantize ``GlyphComponent.transform`` floats to ``F2Dot14`` to fix
  round-trip issue when computing bounding boxes of transformed components (#1830).
- [glyf] If a component uses reference points (``firstPt`` and ``secondPt``) for
  alignment (instead of X and Y offsets), compute the effective translation offset
  *after* having applied any transform (#1831).
- [glyf] When all glyphs have zero contours, compile ``glyf`` table data as a single
  null byte in order to pass validation by OTS and Windows (#1829).
- [feaLib] Parsing feature code now ensures that referenced glyph names are part of
  the known glyph set, unless a glyph set was not provided.
- [varLib] When filling in the default axis value for a missing location of a source or
  instance, correctly map the value forward.
- [varLib] The avar table can now contain mapping output values that are greater than
  OR EQUAL to the preceeding value, as the avar specification allows this.
- [varLib] The errors of the module are now ordered hierarchically below VarLibError.
  See #1821.

4.3.0 (released 2020-02-03)
---------------------------

- [EBLC/CBLC] Fixed incorrect padding length calculation for Format 3 IndexSubTable
  (#1817, #1818).
- [varLib] Fixed error when merging OTL tables and TTFonts were loaded as ``lazy=True``
  (#1808, #1809).
- [varLib] Allow to use master fonts containing ``CFF2`` table when building VF (#1816).
- [ttLib] Make ``recalcBBoxes`` option work also with ``CFF2`` table (#1816).
- [feaLib] Don't reset ``lookupflag`` in lookups defined inside feature blocks.
  They will now inherit the current ``lookupflag`` of the feature. This is what
  Adobe ``makeotf`` also does in this case (#1815).
- [feaLib] Fixed bug with mixed single/multiple substitutions. If a single substitution
  involved a glyph class, we were incorrectly using only the first glyph in the class
  (#1814).

4.2.5 (released 2020-01-29)
---------------------------

- [feaLib] Do not fail on duplicate multiple substitutions, only warn (#1811).
- [subset] Optimize SinglePos subtables to Format 1 if all ValueRecords are the same
  (#1802).

4.2.4 (released 2020-01-09)
---------------------------

- [unicodedata] Update RTL_SCRIPTS for Unicode 11 and 12.

4.2.3 (released 2020-01-07)
---------------------------

- [otTables] Fixed bug when splitting `MarkBasePos` subtables as offsets overflow.
  The mark class values in the split subtable were not being updated, leading to
  invalid mark-base attachments (#1797, googlefonts/noto-source#145).
- [feaLib] Only log a warning instead of error when features contain duplicate
  substitutions (#1767).
- [glifLib] Strip XML comments when parsing with lxml (#1784, #1785).

4.2.2 (released 2019-12-12)
---------------------------

- [subset] Fixed issue with subsetting FeatureVariations table when the index
  of features changes as features get dropped. The feature index need to be
  remapped to point to index of the remaining features (#1777, #1782).
- [fontBuilder] Added `addFeatureVariations` method to `FontBuilder` class. This
  is a shorthand for calling `featureVars.addFeatureVariations` on the builder's
  TTFont object (#1781).
- [glyf] Fixed the flags bug in glyph.drawPoints() like we did for glyph.draw()
  (#1771, #1774).

4.2.1 (released 2019-12-06)
---------------------------

- [glyf] Use the ``flagOnCurve`` bit mask in ``glyph.draw()``, so that we ignore
  the ``overlap`` flag that may be set when instantiating variable fonts (#1771).

4.2.0 (released 2019-11-28)
---------------------------

- [pens] Added the following pens:

  * ``roundingPen.RoundingPen``: filter pen that rounds coordinates and components'
    offsets to integer;
  * ``roundingPen.RoundingPointPen``: like the above, but using PointPen protocol.
  * ``filterPen.FilterPointPen``: base class for filter point pens;
  * ``transformPen.TransformPointPen``: filter point pen to apply affine transform;
  * ``recordingPen.RecordingPointPen``: records and replays point-pen commands.

- [ttGlyphPen] Always round float coordinates and component offsets to integers
  (#1763).
- [ufoLib] When converting kerning groups from UFO2 to UFO3, avoid confusing
  groups with the same name as one of the glyphs (#1761, #1762,
  unified-font-object/ufo-spec#98).

4.1.0 (released 2019-11-18)
---------------------------

- [instancer] Implemented restricting axis ranges (level 3 partial instancing).
  You can now pass ``{axis_tag: (min, max)}`` tuples as input to the
  ``instantiateVariableFont`` function. Note that changing the default axis
  position is not supported yet. The command-line script also accepts axis ranges
  in the form of colon-separated float values, e.g. ``wght=400:700`` (#1753, #1537).
- [instancer] Never drop STAT ``DesignAxis`` records, but only prune out-of-range
  ``AxisValue`` records.
- [otBase/otTables] Enforce that VarStore.RegionAxisCount == fvar.axisCount, even
  when regions list is empty to appease OTS < v8.0 (#1752).
- [designspaceLib] Defined new ``processing`` attribute for ``<rules>`` element,
  with values "first" or "last", plus other editorial changes to DesignSpace
  specification. Bumped format version to 4.1 (#1750).
- [varLib] Improved error message when masters' glyph orders do not match (#1758,
  #1759).
- [featureVars] Allow to specify custom feature tag in ``addFeatureVariations``;
  allow said feature to already exist, in which case we append new lookup indices
  to existing features. Implemented ``<rules>`` attribute ``processing`` according to
  DesignSpace specification update in #1750. Depending on this flag, we generate
  either an 'rvrn' (always processed first) or a 'rclt' feature (follows lookup order,
  therefore last) (#1747, #1625, #1371).
- [ttCollection] Added support for context manager auto-closing via ``with`` statement
  like with ``TTFont`` (#1751).
- [unicodedata] Require unicodedata2 >= 12.1.0.
- [py2.py3] Removed yet more PY2 vestiges (#1743).
- [_n_a_m_e] Fixed issue when comparing NameRecords with different string types (#1742).
- [fixedTools] Changed ``fixedToFloat`` to not do any rounding but simply return
  ``value / (1 << precisionBits)``. Added ``floatToFixedToStr`` and
  ``strToFixedToFloat`` functions to be used when loading from or dumping to XML.
  Fixed values (e.g. fvar axes and instance coordinates, avar mappings, etc.) are
  are now stored as un-rounded decimal floats upon decompiling (#1740, #737).
- [feaLib] Fixed handling of multiple ``LigatureCaret`` statements for the same glyph.
  Only the first rule per glyph is used, additional ones are ignored (#1733).

4.0.2 (released 2019-09-26)
---------------------------

- [voltLib] Added support for ``ALL`` and ``NONE`` in ``PROCESS_MARKS`` (#1732).
- [Silf] Fixed issue in ``Silf`` table compilation and decompilation regarding str vs
  bytes in python3 (#1728).
- [merge] Handle duplicate glyph names better: instead of appending font index to
  all glyph names, use similar code like we use in ``post`` and ``CFF`` tables (#1729).

4.0.1 (released 2019-09-11)
---------------------------

- [otTables] Support fixing offset overflows in ``MultipleSubst`` lookup subtables
  (#1706).
- [subset] Prune empty strikes in ``EBDT`` and ``CBDT`` table data (#1698, #1633).
- [pens] Fixed issue in ``PointToSegmentPen`` when last point of closed contour has
  same coordinates as the starting point and was incorrectly dropped (#1720).
- [Graphite] Fixed ``Sill`` table output to pass OTS (#1705).
- [name] Added ``removeNames`` method to ``table__n_a_m_e`` class (#1719).
- [ttLib] Added aliases for renamed entries ``ascender`` and ``descender`` in
  ``hhea`` table (#1715).

4.0.0 (released 2019-08-22)
---------------------------

- NOTE: The v4.x version series only supports Python 3.6 or greater. You can keep
  using fonttools 3.x if you need support for Python 2.
- [py23] Removed all the python2-only code since it is no longer reachable, thus
  unused; only the Python3 symbols were kept, but these are no-op. The module is now
  DEPRECATED and will removed in the future.
- [ttLib] Fixed UnboundLocalError for empty loca/glyph tables (#1680). Also, allow
  the glyf table to be incomplete when dumping to XML (#1681).
- [varLib.models] Fixed KeyError while sorting masters and there are no on-axis for
  a given axis (38a8eb0e).
- [cffLib] Make sure glyph names are unique (#1699).
- [feaLib] Fix feature parser to correctly handle octal numbers (#1700).

.. package description limit

3.44.0 (released 2019-08-02)
----------------------------

- NOTE: This is the last scheduled release to support Python 2.7. The upcoming fonttools
  v4.x series is going to require Python 3.6 or greater.
- [varLib] Added new ``varLib.instancer`` module for partially instantiating variable
  fonts. This extends (and will eventually replace) ``varLib.mutator`` module, as
  it allows to create not just full static instances from a variable font, but also
  "partial" or "less variable" fonts where some of the axes are dropped or
  instantiated at a particular value.
  Also available from the command-line as `fonttools varLib.instancer --help`
  (#1537, #1628).
- [cffLib] Added support for ``FDSelect`` format 4 (#1677).
- [subset] Added support for subsetting ``sbix`` (Apple bitmap color font) table.
- [t1Lib] Fixed issue parsing ``eexec`` section in Type1 fonts when whitespace
  characters are interspersed among the trailing zeros (#1676).
- [cffLib.specializer] Fixed bug in ``programToCommands`` with CFF2 charstrings (#1669).

3.43.2 (released 2019-07-10)
----------------------------

- [featureVars] Fixed region-merging code on python3 (#1659).
- [varLib.cff] Fixed merging of sparse PrivateDict items (#1653).

3.43.1 (released 2019-06-19)
----------------------------

- [subset] Fixed regression when passing ``--flavor=woff2`` option with an input font
  that was already compressed as WOFF 1.0 (#1650).

3.43.0 (released 2019-06-18)
----------------------------

- [woff2] Added support for compressing/decompressing WOFF2 fonts with non-transformed
  ``glyf`` and ``loca`` tables, as well as with transformed ``hmtx`` table.
  Removed ``Snippets/woff2_compress.py`` and ``Snippets/woff2_decompress.py`` scripts,
  and replaced them with a new console entry point ``fonttools ttLib.woff2``
  that provides two sub-commands ``compress`` and ``decompress``.
- [varLib.cff] Fixed bug when merging CFF2 ``PrivateDicts``. The ``PrivateDict``
  data from the first region font was incorrecty used for all subsequent fonts.
  The bug would only affect variable CFF2 fonts with hinting (#1643, #1644).
  Also, fixed a merging bug when VF masters have no blends or marking glyphs (#1632,
  #1642).
- [loggingTools] Removed unused backport of ``LastResortLogger`` class.
- [subset] Gracefully handle partial MATH table (#1635).
- [featureVars] Avoid duplicate references to ``rvrn`` feature record in
  ``DefaultLangSys`` tables when calling ``addFeatureVariations`` on a font that
  does not already have a ``GSUB`` table (aa8a5bc6).
- [varLib] Fixed merging of class-based kerning. Before, the process could introduce
  rogue kerning values and variations for random classes against class zero (everything
  not otherwise classed).
- [varLib] Fixed merging GPOS tables from master fonts with different number of
  ``SinglePos`` subtables (#1621, #1641).
- [unicodedata] Updated Blocks, Scripts and ScriptExtensions to Unicode 12.1.

3.42.0 (released 2019-05-28)
----------------------------

- [OS/2] Fixed sign of ``fsType``: it should be ``uint16``, not ``int16`` (#1619).
- [subset] Skip out-of-range class values in mark attachment (#1478).
- [fontBuilder] Add an empty ``DSIG`` table with ``setupDummyDSIG`` method (#1621).
- [varLib.merger] Fixed bug whereby ``GDEF.GlyphClassDef`` were being dropped
  when generating instance via ``varLib.mutator`` (#1614).
- [varLib] Added command-line options ``-v`` and ``-q`` to configure logging (#1613).
- [subset] Update font extents in head table (#1612).
- [subset] Make --retain-gids truncate empty glyphs after the last non-empty glyph
  (#1611).
- [requirements] Updated ``unicodedata2`` backport for Unicode 12.0.

3.41.2 (released 2019-05-13)
----------------------------

- [cffLib] Fixed issue when importing a ``CFF2`` variable font from XML, whereby
  the VarStore state was not propagated to PrivateDict (#1598).
- [varLib] Don't drop ``post`` glyph names when building CFF2 variable font (#1609).


3.41.1 (released 2019-05-13)
----------------------------

- [designspaceLib] Added ``loadSourceFonts`` method to load source fonts using
  custom opener function (#1606).
- [head] Round font bounding box coordinates to integers to fix compile error
  if CFF font has float coordinates (#1604, #1605).
- [feaLib] Don't write ``None`` in ``ast.ValueRecord.asFea()`` (#1599).
- [subset] Fixed issue ``AssertionError`` when using ``--desubroutinize`` option
  (#1590, #1594).
- [graphite] Fixed bug in ``Silf`` table's ``decompile`` method unmasked by
  previous typo fix (#1597). Decode languange code as UTF-8 in ``Sill`` table's
  ``decompile`` method (#1600).

3.41.0 (released 2019-04-29)
----------------------------

- [varLib/cffLib] Added support for building ``CFF2`` variable font from sparse
  masters, or masters with more than one model (multiple ``VarStore.VarData``).
  In ``cffLib.specializer``, added support for ``CFF2`` CharStrings with
  ``blend`` operators (#1547, #1591).
- [subset] Fixed subsetting ``HVAR`` and ``VVAR`` with ``--retain-gids`` option,
  and when advances mapping is null while sidebearings mappings are non-null
  (#1587, #1588).
- Added ``otlLib.maxContextCalc`` module to compute ``OS/2.usMaxContext`` value.
  Calculate it automatically when compiling features with feaLib. Added option
  ``--recalc-max-context`` to ``subset`` module (#1582).
- [otBase/otTables] Fixed ``AttributeError`` on missing OT table fields after
  importing font from TTX (#1584).
- [graphite] Fixed typo ``Silf`` table's ``decompile`` method (#1586).
- [otlLib] Better compress ``GPOS`` SinglePos (LookupType 1) subtables (#1539).

3.40.0 (released 2019-04-08)
----------------------------

- [subset] Fixed error while subsetting ``VVAR`` with ``--retain-gids``
  option (#1552).
- [designspaceLib] Use up-to-date default location in ``findDefault`` method
  (#1554).
- [voltLib] Allow passing file-like object to Parser.
- [arrayTools/glyf] ``calcIntBounds`` (used to compute bounding boxes of glyf
  table's glyphs) now uses ``otRound`` instead of ``round3`` (#1566).
- [svgLib] Added support for converting more SVG shapes to path ``d`` strings
  (ellipse, line, polyline), as well as support for ``transform`` attributes.
  Only ``matrix`` transformations are currently supported (#1564, #1564).
- [varLib] Added support for building ``VVAR`` table from ``vmtx`` and ``VORG``
  tables (#1551).
- [fontBuilder] Enable making CFF2 fonts with ``post`` table format 2 (#1557).
- Fixed ``DeprecationWarning`` on invalid escape sequences (#1562).

3.39.0 (released 2019-03-19)
----------------------------

- [ttLib/glyf] Raise more specific error when encountering recursive
  component references (#1545, #1546).
- [Doc/designspaceLib] Defined new ``public.skipExportGlyphs`` lib key (#1534,
  unified-font-object/ufo-spec#84).
- [varLib] Use ``vmtx`` to compute vertical phantom points; or ``hhea.ascent``
  and ``head.unitsPerEM`` if ``vmtx`` is missing (#1528).
- [gvar/cvar] Sort XML element's min/value/max attributes in TupleVariation
  toXML to improve readability of TTX dump (#1527).
- [varLib.plot] Added support for 2D plots with only 1 variation axis (#1522).
- [designspaceLib] Use axes maps when normalizing locations in
  DesignSpaceDocument (#1226, #1521), and when finding default source (#1535).
- [mutator] Set ``OVERLAP_SIMPLE`` and ``OVERLAP_COMPOUND`` glyf flags by
  default in ``instantiateVariableFont``. Added ``--no-overlap`` cli option
  to disable this (#1518).
- [subset] Fixed subsetting ``VVAR`` table (#1516, #1517).
  Fixed subsetting an ``HVAR`` table that has an ``AdvanceWidthMap`` when the
  option ``--retain-gids`` is used.
- [feaLib] Added ``forceChained`` in MultipleSubstStatement (#1511).
  Fixed double indentation of ``subtable`` statement (#1512).
  Added support for ``subtable`` statement in more places than just PairPos
  lookups (#1520).
  Handle lookupflag 0 and lookupflag without a value (#1540).
- [varLib] In ``load_designspace``, provide a default English name for the
  ``ital`` axis tag.
- Remove pyftinspect because it is unmaintained and bitrotted.

3.38.0 (released 2019-02-18)
----------------------------

- [cffLib] Fixed RecursionError when unpickling or deepcopying TTFont with
  CFF table (#1488, 649dc49).
- [subset] Fixed AttributeError when using --desubroutinize option (#1490).
  Also, fixed desubroutinizing bug when subrs contain hints (#1499).
- [CPAL] Make Color a subclass of namedtuple (173a0f5).
- [feaLib] Allow hyphen in glyph class names.
- [feaLib] Added 'tables' option to __main__.py (#1497).
- [feaLib] Add support for special-case contextual positioning formatting
  (#1501).
- [svgLib] Support converting SVG basic shapes (rect, circle, etc.) into
  equivalent SVG paths (#1500, #1508).
- [Snippets] Added name-viewer.ipynb Jupyter notebook.


3.37.3 (released 2019-02-05)
----------------------------

- The previous release accidentally changed several files from Unix to DOS
  line-endings. Fix that.

3.37.2 (released 2019-02-05)
----------------------------

- [varLib] Temporarily revert the fix to ``load_masters()``, which caused a
  crash in ``interpolate_layout()`` when ``deepcopy``-ing OTFs.

3.37.1 (released 2019-02-05)
----------------------------

- [varLib] ``load_masters()`` now actually assigns the fonts it loads to the
  source.font attributes.
- [varLib] Fixed an MVAR table generation crash when sparse masters were
  involved.
- [voltLib] ``parse_coverage_()`` returns a tuple instead of an ast.Enum.
- [feaLib] A MarkClassDefinition inside a block is no longer doubly indented
  compared to the rest of the block.

3.37.0 (released 2019-01-28)
----------------------------

- [svgLib] Added support for converting elliptical arcs to cubic bezier curves
  (#1464).
- [py23] Added backport for ``math.isfinite``.
- [varLib] Apply HIDDEN flag to fvar axis if designspace axis has attribute
  ``hidden=1``.
- Fixed "DeprecationWarning: invalid escape sequence" in Python 3.7.
- [voltLib] Fixed parsing glyph groups. Distinguish different PROCESS_MARKS.
  Accept COMPONENT glyph type.
- [feaLib] Distinguish missing value and explicit ``<NULL>`` for PairPos2
  format A (#1459). Round-trip ``useExtension`` keyword. Implemented
  ``ValueRecord.asFea`` method.
- [subset] Insert empty widths into hdmx when retaining gids (#1458).

3.36.0 (released 2019-01-17)
----------------------------

- [ttx] Added ``--no-recalc-timestamp`` option to keep the original font's
  ``head.modified`` timestamp (#1455, #46).
- [ttx/psCharStrings] Fixed issues while dumping and round-tripping CFF2 table
  with ttx (#1451, #1452, #1456).
- [voltLib] Fixed check for duplicate anchors (#1450). Don't try to read past
  the ``END`` operator in .vtp file (#1453).
- [varLib] Use sentinel value -0x8000 (-32768) to ignore post.underlineThickness
  and post.underlinePosition when generating MVAR deltas (#1449,
  googlei18n/ufo2ft#308).
- [subset] Added ``--retain-gids`` option to subset font without modifying the
  current glyph indices (#1443, #1447).
- [ufoLib] Replace deprecated calls to ``getbytes`` and ``setbytes`` with new
  equivalent ``readbytes`` and ``writebytes`` calls. ``fs`` >= 2.2 no required.
- [varLib] Allow loading masters from TTX files as well (#1441).

3.35.2 (released 2019-01-14)
----------------------------

- [hmtx/vmtx]: Allow to compile/decompile ``hmtx`` and ``vmtx`` tables even
  without the corresponding (required) metrics header tables, ``hhea`` and
  ``vhea`` (#1439).
- [varLib] Added support for localized axes' ``labelname`` and named instances'
  ``stylename`` (#1438).

3.35.1 (released 2019-01-09)
----------------------------

- [_m_a_x_p] Include ``maxComponentElements`` in ``maxp`` table's recalculation.

3.35.0 (released 2019-01-07)
----------------------------

- [psCharStrings] In ``encodeFloat`` function, use float's "general format" with
  8 digits of precision (i.e. ``%8g``) instead of ``str()``. This works around
  a macOS rendering issue when real numbers in CFF table are too long, and
  also makes sure that floats are encoded with the same precision in python 2.7
  and 3.x (#1430, googlei18n/ufo2ft#306).
- [_n_a_m_e/fontBuilder] Make ``_n_a_m_e_table.addMultilingualName`` also add
  Macintosh (platformID=1) names by default. Added options to ``FontBuilder``
  ``setupNameTable`` method to optionally disable Macintosh or Windows names.
  (#1359, #1431).
- [varLib] Make ``build`` optionally accept a ``DesignSpaceDocument`` object,
  instead of a designspace file path. The caller can now set the ``font``
  attribute of designspace's sources to a TTFont object, thus allowing to
  skip filenames manipulation altogether (#1416, #1425).
- [sfnt] Allow SFNTReader objects to be deep-copied.
- Require typing>=3.6.4 on py27 to fix issue with singledispatch (#1423).
- [designspaceLib/t1Lib/macRes] Fixed some cases where pathlib.Path objects were
  not accepted (#1421).
- [varLib] Fixed merging of multiple PairPosFormat2 subtables (#1411).
- [varLib] The default STAT table version is now set to 1.1, to improve
  compatibility with legacy applications (#1413).

3.34.2 (released 2018-12-17)
----------------------------

- [merge] Fixed AssertionError when none of the script tables in GPOS/GSUB have
  a DefaultLangSys record (#1408, 135a4a1).

3.34.1 (released 2018-12-17)
----------------------------

- [varLib] Work around macOS rendering issue for composites without gvar entry (#1381).

3.34.0 (released 2018-12-14)
----------------------------

- [varLib] Support generation of CFF2 variable fonts. ``model.reorderMasters()``
  now supports arbitrary mapping. Fix handling of overlapping ranges for feature
  variations (#1400).
- [cffLib, subset] Code clean-up and fixing related to CFF2 support.
- [ttLib.tables.ttProgram] Use raw strings for regex patterns (#1389).
- [fontbuilder] Initial support for building CFF2 fonts. Set CFF's
  ``FontMatrix`` automatically from unitsPerEm.
- [plistLib] Accept the more general ``collections.Mapping`` instead of the
  specific ``dict`` class to support custom data classes that should serialize
  to dictionaries.

3.33.0 (released 2018-11-30)
----------------------------
- [subset] subsetter bug fix with variable fonts.
- [varLib.featureVar] Improve FeatureVariations generation with many rules.
- [varLib] Enable sparse masters when building variable fonts:
  https://github.com/fonttools/fonttools/pull/1368#issuecomment-437257368
- [varLib.mutator] Add IDEF for GETVARIATION opcode, for handling hints in an
  instance.
- [ttLib] Ignore the length of kern table subtable format 0

3.32.0 (released 2018-11-01)
----------------------------

- [ufoLib] Make ``UFOWriter`` a subclass of ``UFOReader``, and use mixins
  for shared methods (#1344).
- [featureVars] Fixed normalization error when a condition's minimum/maximum
  attributes are missing in designspace ``<rule>`` (#1366).
- [setup.py] Added ``[plot]`` to extras, to optionally install ``matplotlib``,
  needed to use the ``fonTools.varLib.plot`` module.
- [varLib] Take total bounding box into account when resolving model (7ee81c8).
  If multiple axes have the same range ratio, cut across both (62003f4).
- [subset] Don't error if ``STAT`` has no ``AxisValue`` tables.
- [fontBuilder] Added a new submodule which contains a ``FontBuilder`` wrapper
  class around ``TTFont`` that makes it easier to create a working TTF or OTF
  font from scratch with code. NOTE: the API is still experimental and may
  change in future versions.

3.31.0 (released 2018-10-21)
----------------------------

- [ufoLib] Merged the `ufoLib <https://github.com/unified-font-objects/ufoLib>`__
  master branch into a new ``fontTools.ufoLib`` package (#1335, #1095).
  Moved ``ufoLib.pointPen`` module to ``fontTools.pens.pointPen``.
  Moved ``ufoLib.etree`` module to ``fontTools.misc.etree``.
  Moved ``ufoLib.plistlib`` module to ``fontTools.misc.plistlib``.
  To use the new ``fontTools.ufoLib`` module you need to install fonttools
  with the ``[ufo]`` extra, or you can manually install the required additional
  dependencies (cf. README.rst).
- [morx] Support AAT action type to insert glyphs and clean up compilation
  of AAT action tables (4a1871f, 2011ccf).
- [subset] The ``--no-hinting`` on a CFF font now also drops the optional
  hinting keys in Private dict: ``ForceBold``, ``LanguageGroup``, and
  ``ExpansionFactor`` (#1322).
- [subset] Include nameIDs referenced by STAT table (#1327).
- [loggingTools] Added ``msg=None`` argument to
  ``CapturingLogHandler.assertRegex`` (0245f2c).
- [varLib.mutator] Implemented ``FeatureVariations`` instantiation (#1244).
- [g_l_y_f] Added PointPen support to ``_TTGlyph`` objects (#1334).

3.30.0 (released 2018-09-18)
----------------------------

- [feaLib] Skip building noop class PairPos subtables when Coverage is NULL
  (#1318).
- [ttx] Expose the previously reserved bit flag ``OVERLAP_SIMPLE`` of
  glyf table's contour points in the TTX dump. This is used in some
  implementations to specify a non-zero fill with overlapping contours (#1316).
- [ttLib] Added support for decompiling/compiling ``TS1C`` tables containing
  VTT sources for ``cvar`` variation table (#1310).
- [varLib] Use ``fontTools.designspaceLib`` to read DesignSpaceDocument. The
  ``fontTools.varLib.designspace`` module is now deprecated and will be removed
  in future versions. The presence of an explicit ``axes`` element is now
  required in order to build a variable font (#1224, #1313).
- [varLib] Implemented building GSUB FeatureVariations table from the ``rules``
  element of DesignSpace document (#1240, #713, #1314).
- [subset] Added ``--no-layout-closure`` option to not expand the subset with
  the glyphs produced by OpenType layout features. Instead, OpenType features
  will be subset to only rules that are relevant to the otherwise-specified
  glyph set (#43, #1121).

3.29.1 (released 2018-09-10)
----------------------------

- [feaLib] Fixed issue whereby lookups from DFLT/dflt were not included in the
  DFLT/non-dflt language systems (#1307).
- [graphite] Fixed issue on big-endian architectures (e.g. ppc64) (#1311).
- [subset] Added ``--layout-scripts`` option to add/exclude set of OpenType
  layout scripts that will be preserved. By default all scripts are retained
  (``'*'``) (#1303).

3.29.0 (released 2018-07-26)
----------------------------

- [feaLib] In the OTL table builder, when the ``name`` table is excluded
  from the list of tables to be build, skip compiling ``featureNames`` blocks,
  as the records referenced in ``FeatureParams`` table don't exist (68951b7).
- [otBase] Try ``ExtensionLookup`` if other offset-overflow methods fail
  (05f95f0).
- [feaLib] Added support for explicit ``subtable;`` break statements in
  PairPos lookups; previously these were ignored (#1279, #1300, #1302).
- [cffLib.specializer] Make sure the stack depth does not exceed maxstack - 1,
  so that a subroutinizer can insert subroutine calls (#1301,
  https://github.com/googlei18n/ufo2ft/issues/266).
- [otTables] Added support for fixing offset overflow errors occurring inside
  ``MarkBasePos`` subtables (#1297).
- [subset] Write the default output file extension based on ``--flavor`` option,
  or the value of ``TTFont.sfntVersion`` (d7ac0ad).
- [unicodedata] Updated Blocks, Scripts and ScriptExtensions for Unicode 11
  (452c85e).
- [xmlWriter] Added context manager to XMLWriter class to autoclose file
  descriptor on exit (#1290).
- [psCharStrings] Optimize the charstring's bytecode by encoding as integers
  all float values that have no decimal portion (8d7774a).
- [ttFont] Fixed missing import of ``TTLibError`` exception (#1285).
- [feaLib] Allow any languages other than ``dflt`` under ``DFLT`` script
  (#1278, #1292).

3.28.0 (released 2018-06-19)
----------------------------

- [featureVars] Added experimental module to build ``FeatureVariations``
  tables. Still needs to be hooked up to ``varLib.build`` (#1240).
- [fixedTools] Added ``otRound`` to round floats to nearest integer towards
  positive Infinity. This is now used where we deal with visual data like X/Y
  coordinates, advance widths/heights, variation deltas, and similar (#1274,
  #1248).
- [subset] Improved GSUB closure memoize algorithm.
- [varLib.models] Fixed regression in model resolution (180124, #1269).
- [feaLib.ast] Fixed error when converting ``SubtableStatement`` to string
  (#1275).
- [varLib.mutator] Set ``OS/2.usWeightClass`` and ``usWidthClass``, and
  ``post.italicAngle`` based on the 'wght', 'wdth' and 'slnt' axis values
  (#1276, #1264).
- [py23/loggingTools] Don't automatically set ``logging.lastResort`` handler
  on py27. Moved ``LastResortLogger`` to the ``loggingTools`` module (#1277).

3.27.1 (released 2018-06-11)
----------------------------

- [ttGlyphPen] Issue a warning and skip building non-existing components
  (https://github.com/googlei18n/fontmake/issues/411).
- [tests] Fixed issue running ttx_test.py from a tagged commit.

3.27.0 (released 2018-06-11)
----------------------------

- [designspaceLib] Added new ``conditionSet`` element to ``rule`` element in
  designspace document. Bumped ``format`` attribute to ``4.0`` (previously,
  it was formatted as an integer). Removed ``checkDefault``, ``checkAxes``
  methods, and any kind of guessing about the axes when the ``<axes>`` element
  is missing. The default master is expected at the intersection of all default
  values for each axis (#1254, #1255, #1267).
- [cffLib] Fixed issues when compiling CFF2 or converting from CFF when the
  font has an FDArray (#1211, #1271).
- [varLib] Avoid attempting to build ``cvar`` table when ``glyf`` table is not
  present, as is the case for CFF2 fonts.
- [subset] Handle None coverages in MarkGlyphSets; revert commit 02616ab that
  sets empty Coverage tables in MarkGlyphSets to None, to make OTS happy.
- [ttFont] Allow to build glyph order from ``maxp.numGlyphs`` when ``post`` or
  ``cmap`` are missing.
- [ttFont] Added ``__len__`` method to ``_TTGlyphSet``.
- [glyf] Ensure ``GlyphCoordinates`` never overflow signed shorts (#1230).
- [py23] Added alias for ``itertools.izip`` shadowing the built-in ``zip``.
- [loggingTools] Memoize ``log`` property of ``LogMixin`` class (fbab12).
- [ttx] Impoved test coverage (#1261).
- [Snippets] Addded script to append a suffix to all family names in a font.
- [varLib.plot] Make it work with matplotlib >= 2.1 (b38e2b).

3.26.0 (released 2018-05-03)
----------------------------

- [designspace] Added a new optional ``layer`` attribute to the source element,
  and a corresponding ``layerName`` attribute to the ``SourceDescriptor``
  object (#1253).
  Added ``conditionset`` element to the ``rule`` element to the spec, but not
  implemented in designspace reader/writer yet (#1254).
- [varLib.models] Refine modeling one last time (0ecf5c5).
- [otBase] Fixed sharing of tables referred to by different offset sizes
  (795f2f9).
- [subset] Don't drop a GDEF that only has VarStore (fc819d6). Set to None
  empty Coverage tables in MarkGlyphSets (02616ab).
- [varLib]: Added ``--master-finder`` command-line option (#1249).
- [varLib.mutator] Prune fvar nameIDs from instance's name table (#1245).
- [otTables] Allow decompiling bad ClassDef tables with invalid format, with
  warning (#1236).
- [varLib] Make STAT v1.2 and reuse nameIDs from fvar table (#1242).
- [varLib.plot] Show master locations. Set axis limits to -1, +1.
- [subset] Handle HVAR direct mapping. Passthrough 'cvar'.
  Added ``--font-number`` command-line option for collections.
- [t1Lib] Allow a text encoding to be specified when parsing a Type 1 font
  (#1234). Added ``kind`` argument to T1Font constructor (c5c161c).
- [ttLib] Added context manager API to ``TTFont`` class, so it can be used in
  ``with`` statements to auto-close the file when exiting the context (#1232).

3.25.0 (released 2018-04-03)
----------------------------

- [varLib] Improved support-resolution algorithm. Previously, the on-axis
  masters would always cut the space. They don't anymore. That's more
  consistent, and fixes the main issue Erik showed at TYPO Labs 2017.
  Any varfont built that had an unusual master configuration will change
  when rebuilt (42bef17, a523a697,
  https://github.com/googlei18n/fontmake/issues/264).
- [varLib.models] Added a ``main()`` entry point, that takes positions and
  prints model results.
- [varLib.plot] Added new module to plot a designspace's
  VariationModel. Requires ``matplotlib``.
- [varLib.mutator] Added -o option to specify output file path (2ef60fa).
- [otTables] Fixed IndexError while pruning of HVAR pre-write (6b6c34a).
- [varLib.models] Convert delta array to floats if values overflows signed
  short integer (0055f94).

3.24.2 (released 2018-03-26)
----------------------------

- [otBase] Don't fail during ``ValueRecord`` copy if src has more items.
  We drop hinting in the subsetter by simply changing ValueFormat, without
  cleaning up the actual ValueRecords. This was causing assertion error if
  a variable font was subsetted without hinting and then passed directly to
  the mutator for instantiation without first it saving to disk.

3.24.1 (released 2018-03-06)
----------------------------

- [varLib] Don't remap the same ``DeviceTable`` twice in VarStore optimizer
  (#1206).
- [varLib] Add ``--disable-iup`` option to ``fonttools varLib`` script,
  and a ``optimize=True`` keyword argument to ``varLib.build`` function,
  to optionally disable IUP optimization while building varfonts.
- [ttCollection] Fixed issue while decompiling ttc with python3 (#1207).

3.24.0 (released 2018-03-01)
----------------------------

- [ttGlyphPen] Decompose composite glyphs if any components' transform is too
  large to fit a ``F2Dot14`` value, or clamp transform values that are
  (almost) equal to +2.0 to make them fit and avoid decomposing (#1200,
  #1204, #1205).
- [ttx] Added new ``-g`` option to dump glyphs from the ``glyf`` table
  splitted as individual ttx files (#153, #1035, #1132, #1202).
- Copied ``ufoLib.filenames`` module to ``fontTools.misc.filenames``, used
  for the ttx split-glyphs option (#1202).
- [feaLib] Added support for ``cvParameters`` blocks in Character Variant
  feautures ``cv01-cv99`` (#860, #1169).
- [Snippets] Added ``checksum.py`` script to generate/check SHA1 hash of
  ttx files (#1197).
- [varLib.mutator] Fixed issue while instantiating some variable fonts
  whereby the horizontal advance width computed from ``gvar`` phantom points
  could turn up to be negative (#1198).
- [varLib/subset] Fixed issue with subsetting GPOS variation data not
  picking up ``ValueRecord`` ``Device`` objects (54fd71f).
- [feaLib/voltLib] In all AST elements, the ``location`` is no longer a
  required positional argument, but an optional kewyord argument (defaults
  to ``None``). This will make it easier to construct feature AST from
  code (#1201).


3.23.0 (released 2018-02-26)
----------------------------

- [designspaceLib] Added an optional ``lib`` element to the designspace as a
  whole, as well as to the instance elements, to store arbitrary data in a
  property list dictionary, similar to the UFO's ``lib``. Added an optional
  ``font`` attribute to the ``SourceDescriptor``, to allow operating on
  in-memory font objects (#1175).
- [cffLib] Fixed issue with lazy-loading of attributes when attempting to
  set the CFF TopDict.Encoding (#1177, #1187).
- [ttx] Fixed regression introduced in 3.22.0 that affected the split tables
  ``-s`` option (#1188).
- [feaLib] Added ``IncludedFeaNotFound`` custom exception subclass, raised
  when an included feature file cannot be found (#1186).
- [otTables] Changed ``VarIdxMap`` to use glyph names internally instead of
  glyph indexes. The old ttx dumps of HVAR/VVAR tables that contain indexes
  can still be imported (21cbab8, 38a0ffb).
- [varLib] Implemented VarStore optimizer (#1184).
- [subset] Implemented pruning of GDEF VarStore, HVAR and MVAR (#1179).
- [sfnt] Restore backward compatiblity with ``numFonts`` attribute of
  ``SFNTReader`` object (#1181).
- [merge] Initial support for merging ``LangSysRecords`` (#1180).
- [ttCollection] don't seek(0) when writing to possibly unseekable strems.
- [subset] Keep all ``--name-IDs`` from 0 to 6 by default (#1170, #605, #114).
- [cffLib] Added ``width`` module to calculate optimal CFF default and
  nominal glyph widths.
- [varLib] Don’t fail if STAT already in the master fonts (#1166).

3.22.0 (released 2018-02-04)
----------------------------

- [subset] Support subsetting ``endchar`` acting as ``seac``-like components
  in ``CFF`` (fixes #1162).
- [feaLib] Allow to build from pre-parsed ``ast.FeatureFile`` object.
  Added ``tables`` argument to only build some tables instead of all (#1159,
  #1163).
- [textTools] Replaced ``safeEval`` with ``ast.literal_eval`` (#1139).
- [feaLib] Added option to the parser to not resolve ``include`` statements
  (#1154).
- [ttLib] Added new ``ttCollection`` module to read/write TrueType and
  OpenType Collections. Exports a ``TTCollection`` class with a ``fonts``
  attribute containing a list of ``TTFont`` instances, the methods ``save``
  and ``saveXML``, plus some list-like methods. The ``importXML`` method is
  not implemented yet (#17).
- [unicodeadata] Added ``ot_tag_to_script`` function that converts from
  OpenType script tag to Unicode script code.
- Added new ``designspaceLib`` subpackage, originally from Erik Van Blokland's
  ``designSpaceDocument``: https://github.com/LettError/designSpaceDocument
  NOTE: this is not yet used internally by varLib, and the API may be subject
  to changes (#911, #1110, LettError/designSpaceDocument#28).
- Added new FontTools icon images (8ee7c32).
- [unicodedata] Added ``script_horizontal_direction`` function that returns
  either "LTR" or "RTL" given a unicode script code.
- [otConverters] Don't write descriptive name string as XML comment if the
  NameID value is 0 (== NULL) (#1151, #1152).
- [unicodedata] Add ``ot_tags_from_script`` function to get the list of
  OpenType script tags associated with unicode script code (#1150).
- [feaLib] Don't error when "enumerated" kern pairs conflict with preceding
  single pairs; emit warning and chose the first value (#1147, #1148).
- [loggingTools] In ``CapturingLogHandler.assertRegex`` method, match the
  fully formatted log message.
- [sbix] Fixed TypeError when concatenating str and bytes (#1154).
- [bezierTools] Implemented cusp support and removed ``approximate_fallback``
  arg in ``calcQuadraticArcLength``. Added ``calcCubicArcLength`` (#1142).

3.21.2 (released 2018-01-08)
----------------------------

- [varLib] Fixed merging PairPos Format1/2 with missing subtables (#1125).

3.21.1 (released 2018-01-03)
----------------------------

- [feaLib] Allow mixed single/multiple substitutions (#612)
- Added missing ``*.afm`` test assets to MAINFEST.in (#1137).
- Fixed dumping ``SVG`` tables containing color palettes (#1124).

3.21.0 (released 2017-12-18)
----------------------------

- [cmap] when compiling format6 subtable, don't assume gid0 is always called
  '.notdef' (1e42224).
- [ot] Allow decompiling fonts with bad Coverage format number (1aafae8).
- Change FontTools licence to MIT (#1127).
- [post] Prune extra names already in standard Mac set (df1e8c7).
- [subset] Delete empty SubrsIndex after subsetting (#994, #1118).
- [varLib] Don't share points in cvar by default, as it currently fails on
  some browsers (#1113).
- [afmLib] Make poor old afmLib work on python3.

3.20.1 (released 2017-11-22)
----------------------------

- [unicodedata] Fixed issue with ``script`` and ``script_extension`` functions
  returning inconsistent short vs long names. They both return the short four-
  letter script codes now. Added ``script_name`` and ``script_code`` functions
  to look up the long human-readable script name from the script code, and
  viceversa (#1109, #1111).

3.20.0 (released 2017-11-21)
----------------------------

- [unicodedata] Addded new module ``fontTools.unicodedata`` which exports the
  same interface as the built-in ``unicodedata`` module, with the addition of
  a few functions that are missing from the latter, such as ``script``,
  ``script_extension`` and ``block``. Added a ``MetaTools/buildUCD.py`` script
  to download and parse data files from the Unicode Character Database and
  generate python modules containing lists of ranges and property values.
- [feaLib] Added ``__str__`` method to all ``ast`` elements (delegates to the
  ``asFea`` method).
- [feaLib] ``Parser`` constructor now accepts a ``glyphNames`` iterable
  instead of ``glyphMap`` dict. The latter still works but with a pending
  deprecation warning (#1104).
- [bezierTools] Added arc length calculation functions originally from
  ``pens.perimeterPen`` module (#1101).
- [varLib] Started generating STAT table (8af4309). Right now it just reflects
  the axes, and even that with certain limitations:
  * AxisOrdering is set to the order axes are defined,
  * Name-table entries are not shared with fvar.
- [py23] Added backports for ``redirect_stdout`` and ``redirect_stderr``
  context managers (#1097).
- [Graphite] Fixed some round-trip bugs (#1093).

3.19.0 (released 2017-11-06)
----------------------------

- [varLib] Try set of used points instead of all points when testing whether to
  share points between tuples (#1090).
- [CFF2] Fixed issue with reading/writing PrivateDict BlueValues to TTX file.
  Read the commit message 8b02b5a and issue #1030 for more details.
  NOTE: this change invalidates all the TTX files containing CFF2 tables
  that where dumped with previous verisons of fonttools.
  CFF2 Subr items can have values on the stack after the last operator, thus
  a ``CFF2Subr`` class was added to accommodate this (#1091).
- [_k_e_r_n] Fixed compilation of AAT kern version=1.0 tables (#1089, #1094)
- [ttLib] Added getBestCmap() convenience method to TTFont class and cmap table
  class that returns a preferred Unicode cmap subtable given a list of options
  (#1092).
- [morx] Emit more meaningful subtable flags. Implement InsertionMorphAction

3.18.0 (released 2017-10-30)
----------------------------

- [feaLib] Fixed writing back nested glyph classes (#1086).
- [TupleVariation] Reactivated shared points logic, bugfixes (#1009).
- [AAT] Implemented ``morx`` ligature subtables (#1082).
- [reverseContourPen] Keep duplicate lineTo following a moveTo (#1080,
  https://github.com/googlei18n/cu2qu/issues/51).
- [varLib.mutator] Suport instantiation of GPOS, GDEF and MVAR (#1079).
- [sstruct] Fixed issue with ``unicode_literals`` and ``struct`` module in
  old versions of python 2.7 (#993).

3.17.0 (released 2017-10-16)
----------------------------

- [svgPathPen] Added an ``SVGPathPen`` that translates segment pen commands
  into SVG path descriptions. Copied from Tal Leming's ``ufo2svg.svgPathPen``
  https://github.com/typesupply/ufo2svg/blob/d69f992/Lib/ufo2svg/svgPathPen.py
- [reverseContourPen] Added ``ReverseContourPen``, a filter pen that draws
  contours with the winding direction reversed, while keeping the starting
  point (#1071).
- [filterPen] Added ``ContourFilterPen`` to manipulate contours as a whole
  rather than segment by segment.
- [arrayTools] Added ``Vector`` class to apply math operations on an array
  of numbers, and ``pairwise`` function to loop over pairs of items in an
  iterable.
- [varLib] Added support for building and interpolation of ``cvar`` table
  (f874cf6, a25a401).

3.16.0 (released 2017-10-03)
----------------------------

- [head] Try using ``SOURCE_DATE_EPOCH`` environment variable when setting
  the ``head`` modified timestamp to ensure reproducible builds (#1063).
  See https://reproducible-builds.org/specs/source-date-epoch/
- [VTT] Decode VTT's ``TSI*`` tables text as UTF-8 (#1060).
- Added support for Graphite font tables: Feat, Glat, Gloc, Silf and Sill.
  Thanks @mhosken! (#1054).
- [varLib] Default to using axis "name" attribute if "labelname" element
  is missing (588f524).
- [merge] Added support for merging Script records. Remove unused features
  and lookups after merge (d802580, 556508b).
- Added ``fontTools.svgLib`` package. Includes a parser for SVG Paths that
  supports the Pen protocol (#1051). Also, added a snippet to convert SVG
  outlines to UFO GLIF (#1053).
- [AAT] Added support for ``ankr``, ``bsln``, ``mort``, ``morx``, ``gcid``,
  and ``cidg``.
- [subset] Implemented subsetting of ``prop``, ``opbd``, ``bsln``, ``lcar``.

3.15.1 (released 2017-08-18)
----------------------------

- [otConverters] Implemented ``__add__`` and ``__radd__`` methods on
  ``otConverters._LazyList`` that decompile a lazy list before adding
  it to another list or ``_LazyList`` instance. Fixes an ``AttributeError``
  in the ``subset`` module when attempting to sum ``_LazyList`` objects
  (6ef48bd2, 1aef1683).
- [AAT] Support the `opbd` table with optical bounds (a47f6588).
- [AAT] Support `prop` table with glyph properties (d05617b4).


3.15.0 (released 2017-08-17)
----------------------------

- [AAT] Added support for AAT lookups. The ``lcar`` table can be decompiled
  and recompiled; futher work needed to handle ``morx`` table (#1025).
- [subset] Keep (empty) DefaultLangSys for Script 'DFLT' (6eb807b5).
- [subset] Support GSUB/GPOS.FeatureVariations (fe01d87b).
- [varLib] In ``models.supportScalars``, ignore an axis when its peak value
  is 0 (fixes #1020).
- [varLib] Add default mappings to all axes in avar to fix rendering issue
  in some rasterizers (19c4b377, 04eacf13).
- [varLib] Flatten multiple tail PairPosFormat2 subtables before merging
  (c55ef525).
- [ttLib] Added support for recalculating font bounding box in ``CFF`` and
  ``head`` tables, and min/max values in ``hhea`` and ``vhea`` tables (#970).

3.14.0 (released 2017-07-31)
----------------------------

- [varLib.merger] Remove Extensions subtables before merging (f7c20cf8).
- [varLib] Initialize the avar segment map with required default entries
  (#1014).
- [varLib] Implemented optimal IUP optmiziation (#1019).
- [otData] Add ``AxisValueFormat4`` for STAT table v1.2 from OT v1.8.2
  (#1015).
- [name] Fixed BCP46 language tag for Mac langID=9: 'si' -> 'sl'.
- [subset] Return value from ``_DehintingT2Decompiler.op_hintmask``
  (c0d672ba).
- [cffLib] Allow to get TopDict by index as well as by name (dca96c9c).
- [cffLib] Removed global ``isCFF2`` state; use one set of classes for
  both CFF and CFF2, maintaining backward compatibility existing code (#1007).
- [cffLib] Deprecated maxstack operator, per OpenType spec update 1.8.1.
- [cffLib] Added missing default (-100) for UnderlinePosition (#983).
- [feaLib] Enable setting nameIDs greater than 255 (#1003).
- [varLib] Recalculate ValueFormat when merging SinglePos (#996).
- [varLib] Do not emit MVAR if there are no entries in the variation store
  (#987).
- [ttx] For ``-x`` option, pad with space if table tag length is < 4.

3.13.1 (released 2017-05-30)
----------------------------

- [feaLib.builder] Removed duplicate lookups optimization. The original
  lookup order and semantics of the feature file are preserved (#976).

3.13.0 (released 2017-05-24)
----------------------------

- [varLib.mutator] Implement IUP optimization (#969).
- [_g_l_y_f.GlyphCoordinates] Changed ``__bool__()`` semantics to match those
  of other iterables (e46f949). Removed ``__abs__()`` (3db5be2).
- [varLib.interpolate_layout] Added ``mapped`` keyword argument to
  ``interpolate_layout`` to allow disabling avar mapping: if False (default),
  the location is mapped using the map element of the axes in designspace file;
  if True, it is assumed that location is in designspace's internal space and
  no mapping is performed (#950, #975).
- [varLib.interpolate_layout] Import designspace-loading logic from varLib.
- [varLib] Fixed bug with recombining PairPosClass2 subtables (81498e5, #914).
- [cffLib.specializer] When copying iterables, cast to list (462b7f86).

3.12.1 (released 2017-05-18)
----------------------------

- [pens.t2CharStringPen] Fixed AttributeError when calling addComponent in
  T2CharStringPen (#965).

3.12.0 (released 2017-05-17)
----------------------------

- [cffLib.specializer] Added new ``specializer`` module to optimize CFF
  charstrings, used by the T2CharStringPen (#948).
- [varLib.mutator] Sort glyphs by component depth before calculating composite
  glyphs' bounding boxes to ensure deltas are correctly caclulated (#945).
- [_g_l_y_f] Fixed loss of precision in GlyphCoordinates by using 'd' (double)
  instead of 'f' (float) as ``array.array`` typecode (#963, #964).

3.11.0 (released 2017-05-03)
----------------------------

- [t2CharStringPen] Initial support for specialized Type2 path operators:
  vmoveto, hmoveto, vlineto, hlineto, vvcurveto, hhcurveto, vhcurveto and
  hvcurveto. This should produce more compact charstrings (#940, #403).
- [Doc] Added Sphinx sources for the documentation. Thanks @gferreira (#935).
- [fvar] Expose flags in XML (#932)
- [name] Add helper function for building multi-lingual names (#921)
- [varLib] Fixed kern merging when a PairPosFormat2 has ClassDef1 with glyphs
  that are NOT present in the Coverage (1b5e1c4, #939).
- [varLib] Fixed non-deterministic ClassDef order with PY3 (f056c12, #927).
- [feLib] Throw an error when the same glyph is defined in multiple mark
  classes within the same lookup (3e3ff00, #453).

3.10.0 (released 2017-04-14)
----------------------------

- [varLib] Added support for building ``avar`` table, using the designspace
  ``<map>`` elements.
- [varLib] Removed unused ``build(..., axisMap)`` argument. Axis map should
  be specified in designspace file now. We do not accept nonstandard axes
  if ``<axes>`` element is not present.
- [varLib] Removed "custom" axis from the ``standard_axis_map``. This was
  added before when glyphsLib was always exporting the (unused) custom axis.
- [varLib] Added partial support for building ``MVAR`` table; does not
  implement ``gasp`` table variations yet.
- [pens] Added FilterPen base class, for pens that control another pen;
  factored out ``addComponent`` method from BasePen into a separate abstract
  DecomposingPen class; added DecomposingRecordingPen, which records
  components decomposed as regular contours.
- [TSI1] Fixed computation of the textLength of VTT private tables (#913).
- [loggingTools] Added ``LogMixin`` class providing a ``log`` property to
  subclasses, which returns a ``logging.Logger`` named after the latter.
- [loggingTools] Added ``assertRegex`` method to ``CapturingLogHandler``.
- [py23] Added backport for python 3's ``types.SimpleNamespace`` class.
- [EBLC] Fixed issue with python 3 ``zip`` iterator.

3.9.2 (released 2017-04-08)
---------------------------

- [pens] Added pen to draw glyphs using WxPython ``GraphicsPath`` class:
  https://wxpython.org/docs/api/wx.GraphicsPath-class.html
- [varLib.merger] Fixed issue with recombining multiple PairPosFormat2
  subtables (#888)
- [varLib] Do not encode gvar deltas that are all zeroes, or if all values
  are smaller than tolerance.
- [ttLib] _TTGlyphSet glyphs now also have ``height`` and ``tsb`` (top
  side bearing) attributes from the ``vmtx`` table, if present.
- [glyf] In ``GlyphCoordintes`` class, added ``__bool__`` / ``__nonzero__``
  methods, and ``array`` property to get raw array.
- [ttx] Support reading TTX files with BOM (#896)
- [CFF2] Fixed the reporting of the number of regions in the font.

3.9.1 (released 2017-03-20)
---------------------------

- [varLib.merger] Fixed issue while recombining multiple PairPosFormat2
  subtables if they were split because of offset overflows (9798c30).
- [varLib.merger] Only merge multiple PairPosFormat1 subtables if there is
  at least one of the fonts with a non-empty Format1 subtable (0f5a46b).
- [varLib.merger] Fixed IndexError with empty ClassDef1 in PairPosFormat2
  (aad0d46).
- [varLib.merger] Avoid reusing Class2Record (mutable) objects (e6125b3).
- [varLib.merger] Calculate ClassDef1 and ClassDef2's Format when merging
  PairPosFormat2 (23511fd).
- [macUtils] Added missing ttLib import (b05f203).

3.9.0 (released 2017-03-13)
---------------------------

- [feaLib] Added (partial) support for parsing feature file comments ``# ...``
  appearing in between statements (#879).
- [feaLib] Cleaned up syntax tree for FeatureNames.
- [ttLib] Added support for reading/writing ``CFF2`` table (thanks to
  @readroberts at Adobe), and ``TTFA`` (ttfautohint) table.
- [varLib] Fixed regression introduced with 3.8.0 in the calculation of
  ``NumShorts``, i.e. the number of deltas in ItemVariationData's delta sets
  that use a 16-bit representation (b2825ff).

3.8.0 (released 2017-03-05)
---------------------------

- New pens: MomentsPen, StatisticsPen, RecordingPen, and TeePen.
- [misc] Added new ``fontTools.misc.symfont`` module, for symbolic font
  statistical analysis; requires ``sympy`` (http://www.sympy.org/en/index.html)
- [varLib] Added experimental ``fontTools.varLib.interpolatable`` module for
  finding wrong contour order between different masters
- [varLib] designspace.load() now returns a dictionary, instead of a tuple,
  and supports <axes> element (#864); the 'masters' item was renamed 'sources',
  like the <sources> element in the designspace document
- [ttLib] Fixed issue with recalculating ``head`` modified timestamp when
  saving CFF fonts
- [ttLib] In TupleVariation, round deltas before compiling (#861, fixed #592)
- [feaLib] Ignore duplicate glyphs in classes used as MarkFilteringSet and
  MarkAttachmentType (#863)
- [merge] Changed the ``gasp`` table merge logic so that only the one from
  the first font is retained, similar to other hinting tables (#862)
- [Tests] Added tests for the ``varLib`` package, as well as test fonts
  from the "Annotated OpenType Specification" (AOTS) to exercise ``ttLib``'s
  table readers/writers (<https://github.com/adobe-type-tools/aots>)

3.7.2 (released 2017-02-17)
---------------------------

- [subset] Keep advance widths when stripping ".notdef" glyph outline in
  CID-keyed CFF fonts (#845)
- [feaLib] Zero values now produce the same results as makeotf (#633, #848)
- [feaLib] More compact encoding for “Contextual positioning with in-line
  single positioning rules” (#514)

3.7.1 (released 2017-02-15)
---------------------------

- [subset] Fixed issue with ``--no-hinting`` option whereby advance widths in
  Type 2 charstrings were also being stripped (#709, #343)
- [feaLib] include statements now resolve relative paths like makeotf (#838)
- [feaLib] table ``name`` now handles Unicode codepoints beyond the Basic
  Multilingual Plane, also supports old-style MacOS platform encodings (#842)
- [feaLib] correctly escape string literals when emitting feature syntax (#780)

3.7.0 (released 2017-02-11)
---------------------------

- [ttx, mtiLib] Preserve ordering of glyph alternates in GSUB type 3 (#833).
- [feaLib] Glyph names can have dashes, as per new AFDKO syntax v1.20 (#559).
- [feaLib] feaLib.Parser now needs the font's glyph map for parsing.
- [varLib] Fix regression where GPOS values were stored as 0.
- [varLib] Allow merging of class-based kerning when ClassDefs are different

3.6.3 (released 2017-02-06)
---------------------------

- [varLib] Fix building variation of PairPosFormat2 (b5c34ce).
- Populate defaults even for otTables that have postRead (e45297b).
- Fix compiling of MultipleSubstFormat1 with zero 'out' glyphs (b887860).

3.6.2 (released 2017-01-30)
---------------------------

- [varLib.merger] Fixed "TypeError: reduce() of empty sequence with no
  initial value" (3717dc6).

3.6.1 (released 2017-01-28)
---------------------------

-  [py23] Fixed unhandled exception occurring at interpreter shutdown in
   the "last resort" logging handler (972b3e6).
-  [agl] Ensure all glyph names are of native 'str' type; avoid mixing
   'str' and 'unicode' in TTFont.glyphOrder (d8c4058).
-  Fixed inconsistent title levels in README.rst that caused PyPI to
   incorrectly render the reStructuredText page.

3.6.0 (released 2017-01-26)
---------------------------

-  [varLib] Refactored and improved the variation-font-building process.
-  Assembly code in the fpgm, prep, and glyf tables is now indented in
   XML output for improved readability. The ``instruction`` element is
   written as a simple tag if empty (#819).
-  [ttx] Fixed 'I/O operation on closed file' error when dumping
   multiple TTXs to standard output with the '-o -' option.
-  The unit test modules (``*_test.py``) have been moved outside of the
   fontTools package to the Tests folder, thus they are no longer
   installed (#811).

3.5.0 (released 2017-01-14)
---------------------------

-  Font tables read from XML can now be written back to XML with no
   loss.
-  GSUB/GPOS LookupType is written out in XML as an element, not
   comment. (#792)
-  When parsing cmap table, do not store items mapped to glyph id 0.
   (#790)
-  [otlLib] Make ClassDef sorting deterministic. Fixes #766 (7d1ddb2)
-  [mtiLib] Added unit tests (#787)
-  [cvar] Implemented cvar table
-  [gvar] Renamed GlyphVariation to TupleVariation to match OpenType
   terminology.
-  [otTables] Handle gracefully empty VarData.Item array when compiling
   XML. (#797)
-  [varLib] Re-enabled generation of ``HVAR`` table for fonts with
   TrueType outlines; removed ``--build-HVAR`` command-line option.
-  [feaLib] The parser can now be extended to support non-standard
   statements in FEA code by using a customized Abstract Syntax Tree.
   See, for example, ``feaLib.builder_test.test_extensions`` and
   baseClass.feax (#794, fixes #773).
-  [feaLib] Added ``feaLib`` command to the 'fonttools' command-line
   tool; applies a feature file to a font. ``fonttools feaLib -h`` for
   help.
-  [pens] The ``T2CharStringPen`` now takes an optional
   ``roundTolerance`` argument to control the rounding of coordinates
   (#804, fixes #769).
-  [ci] Measure test coverage on all supported python versions and OSes,
   combine coverage data and upload to
   https://codecov.io/gh/fonttools/fonttools (#786)
-  [ci] Configured Travis and Appveyor for running tests on Python 3.6
   (#785, 55c03bc)
-  The manual pages installation directory can be customized through
   ``FONTTOOLS_MANPATH`` environment variable (#799, fixes #84).
-  [Snippets] Added otf2ttf.py, for converting fonts from CFF to
   TrueType using the googlei18n/cu2qu module (#802)

3.4.0 (released 2016-12-21)
---------------------------

-  [feaLib] Added support for generating FEA text from abstract syntax
   tree (AST) objects (#776). Thanks @mhosken
-  Added ``agl.toUnicode`` function to convert AGL-compliant glyph names
   to Unicode strings (#774)
-  Implemented MVAR table (b4d5381)

3.3.1 (released 2016-12-15)
---------------------------

-  [setup] We no longer use versioneer.py to compute fonttools version
   from git metadata, as this has caused issues for some users (#767).
   Now we bump the version strings manually with a custom ``release``
   command of setup.py script.

3.3.0 (released 2016-12-06)
---------------------------

-  [ttLib] Implemented STAT table from OpenType 1.8 (#758)
-  [cffLib] Fixed decompilation of CFF fonts containing non-standard
   key/value pairs in FontDict (issue #740; PR #744)
-  [py23] minor: in ``round3`` function, allow the second argument to be
   ``None`` (#757)
-  The standalone ``sstruct`` and ``xmlWriter`` modules, deprecated
   since vesion 3.2.0, have been removed. They can be imported from the
   ``fontTools.misc`` package.

3.2.3 (released 2016-12-02)
---------------------------

-  [py23] optimized performance of round3 function; added backport for
   py35 math.isclose() (9d8dacb)
-  [subset] fixed issue with 'narrow' (UCS-2) Python 2 builds and
   ``--text``/``--text-file`` options containing non-BMP chararcters
   (16d0e5e)
-  [varLib] fixed issuewhen normalizing location values (8fa2ee1, #749)
-  [inspect] Made it compatible with both python2 and python3 (167ee60,
   #748). Thanks @pnemade

3.2.2 (released 2016-11-24)
---------------------------

-  [varLib] Do not emit null axes in fvar (1bebcec). Thanks @robmck-ms
-  [varLib] Handle fonts without GPOS (7915a45)
-  [merge] Ignore LangSys if None (a11bc56)
-  [subset] Fix subsetting MathVariants (78d3cbe)
-  [OS/2] Fix "Private Use (plane 15)" range (08a0d55). Thanks @mashabow

3.2.1 (released 2016-11-03)
---------------------------

-  [OS/2] fix checking ``fsSelection`` bits matching ``head.macStyle``
   bits
-  [varLib] added ``--build-HVAR`` option to generate ``HVAR`` table for
   fonts with TrueType outlines. For ``CFF2``, it is enabled by default.

3.2.0 (released 2016-11-02)
---------------------------

-  [varLib] Improve support for OpenType 1.8 Variable Fonts:
-  Implement GDEF's VariationStore
-  Implement HVAR/VVAR tables
-  Partial support for loading MutatorMath .designspace files with
   varLib.designspace module
-  Add varLib.models with Variation fonts interpolation models
-  Implement GSUB/GPOS FeatureVariations
-  Initial support for interpolating and merging OpenType Layout tables
   (see ``varLib.interpolate_layout`` and ``varLib.merger`` modules)
-  [API change] Change version to be an integer instead of a float in
   XML output for GSUB, GPOS, GDEF, MATH, BASE, JSTF, HVAR, VVAR, feat,
   hhea and vhea tables. Scripts that set the Version for those to 1.0
   or other float values also need fixing. A warning is emitted when
   code or XML needs fix.
-  several bug fixes to the cffLib module, contributed by Adobe's
   @readroberts
-  The XML output for CFF table now has a 'major' and 'minor' elements
   for specifying whether it's version 1.0 or 2.0 (support for CFF2 is
   coming soon)
-  [setup.py] remove undocumented/deprecated ``extra_path`` Distutils
   argument. This means that we no longer create a "FontTools" subfolder
   in site-packages containing the actual fontTools package, as well as
   the standalone xmlWriter and sstruct modules. The latter modules are
   also deprecated, and scheduled for removal in upcoming releases.
   Please change your import statements to point to from fontTools.misc
   import xmlWriter and from fontTools.misc import sstruct.
-  [scripts] Add a 'fonttools' command-line tool that simply runs
   ``fontTools.*`` sub-modules: e.g. ``fonttools ttx``,
   ``fonttools subset``, etc.
-  [hmtx/vmts] Read advance width/heights as unsigned short (uint16);
   automatically round float values to integers.
-  [ttLib/xmlWriter] add 'newlinestr=None' keyword argument to
   ``TTFont.saveXML`` for overriding os-specific line endings (passed on
   to ``XMLWriter`` instances).
-  [versioning] Use versioneer instead of ``setuptools_scm`` to
   dynamically load version info from a git checkout at import time.
-  [feaLib] Support backslash-prefixed glyph names.

3.1.2 (released 2016-09-27)
---------------------------

-  restore Makefile as an alternative way to build/check/install
-  README.md: update instructions for installing package from source,
   and for running test suite
-  NEWS: Change log was out of sync with tagged release

3.1.1 (released 2016-09-27)
---------------------------

-  Fix ``ttLibVersion`` attribute in TTX files still showing '3.0'
   instead of '3.1'.
-  Use ``setuptools_scm`` to manage package versions.

3.1.0 (released 2016-09-26)
---------------------------

-  [feaLib] New library to parse and compile Adobe FDK OpenType Feature
   files.
-  [mtiLib] New library to parse and compile Monotype 'FontDame'
   OpenType Layout Tables files.
-  [voltLib] New library to parse Microsoft VOLT project files.
-  [otlLib] New library to work with OpenType Layout tables.
-  [varLib] New library to work with OpenType Font Variations.
-  [pens] Add ttGlyphPen to draw to TrueType glyphs, and t2CharStringPen
   to draw to Type 2 Charstrings (CFF); add areaPen and perimeterPen.
-  [ttLib.tables] Implement 'meta' and 'trak' tables.
-  [ttx] Add --flavor option for compiling to 'woff' or 'woff2'; add
   ``--with-zopfli`` option to use Zopfli to compress WOFF 1.0 fonts.
-  [subset] Support subsetting 'COLR'/'CPAL' and 'CBDT'/'CBLC' color
   fonts tables, and 'gvar' table for variation fonts.
-  [Snippets] Add ``symfont.py``, for symbolic font statistics analysis;
   interpolatable.py, a preliminary script for detecting interpolation
   errors; ``{merge,dump}_woff_metadata.py``.
-  [classifyTools] Helpers to classify things into classes.
-  [CI] Run tests on Windows, Linux and macOS using Appveyor and Travis
   CI; check unit test coverage with Coverage.py/Coveralls; automatic
   deployment to PyPI on tags.
-  [loggingTools] Use Python built-in logging module to print messages.
-  [py23] Make round() behave like Python 3 built-in round(); define
   round2() and round3().

3.0 (released 2015-09-01)
-------------------------

-  Add Snippet scripts for cmap subtable format conversion, printing
   GSUB/GPOS features, building a GX font from two masters
-  TTX WOFF2 support and a ``-f`` option to overwrite output file(s)
-  Support GX tables: ``avar``, ``gvar``, ``fvar``, ``meta``
-  Support ``feat`` and gzip-compressed SVG tables
-  Upgrade Mac East Asian encodings to native implementation if
   available
-  Add Roman Croatian and Romanian encodings, codecs for mac-extended
   East Asian encodings
-  Implement optimal GLYF glyph outline packing; disabled by default

2.5 (released 2014-09-24)
-------------------------

-  Add a Qt pen
-  Add VDMX table converter
-  Load all OpenType sub-structures lazily
-  Add support for cmap format 13.
-  Add pyftmerge tool
-  Update to Unicode 6.3.0d3
-  Add pyftinspect tool
-  Add support for Google CBLC/CBDT color bitmaps, standard EBLC/EBDT
   embedded bitmaps, and ``SVG`` table (thanks to Read Roberts at Adobe)
-  Add support for loading, saving and ttx'ing WOFF file format
-  Add support for Microsoft COLR/CPAL layered color glyphs
-  Support PyPy
-  Support Jython, by replacing numpy with array/lists modules and
   removed it, pure-Python StringIO, not cStringIO
-  Add pyftsubset and Subsetter object, supporting CFF and TTF
-  Add to ttx args for -q for quiet mode, -z to choose a bitmap dump
   format

2.4 (released 2013-06-22)
-------------------------

-  Option to write to arbitrary files
-  Better dump format for DSIG
-  Better detection of OTF XML
-  Fix issue with Apple's kern table format
-  Fix mangling of TT glyph programs
-  Fix issues related to mona.ttf
-  Fix Windows Installer instructions
-  Fix some modern MacOS issues
-  Fix minor issues and typos

2.3 (released 2009-11-08)
-------------------------

-  TrueType Collection (TTC) support
-  Python 2.6 support
-  Update Unicode data to 5.2.0
-  Couple of bug fixes

2.2 (released 2008-05-18)
-------------------------

-  ClearType support
-  cmap format 1 support
-  PFA font support
-  Switched from Numeric to numpy
-  Update Unicode data to 5.1.0
-  Update AGLFN data to 1.6
-  Many bug fixes

2.1 (released 2008-01-28)
-------------------------

-  Many years worth of fixes and features

2.0b2 (released 2002-??-??)
---------------------------

-  Be "forgiving" when interpreting the maxp table version field:
   interpret any value as 1.0 if it's not 0.5. Fixes dumping of these
   GPL fonts: http://www.freebsd.org/cgi/pds.cgi?ports/chinese/wangttf
-  Fixed ttx -l: it turned out this part of the code didn't work with
   Python 2.2.1 and earlier. My bad to do most of my testing with a
   different version than I shipped TTX with :-(
-  Fixed bug in ClassDef format 1 subtable (Andreas Seidel bumped into
   this one).

2.0b1 (released 2002-09-10)
---------------------------

-  Fixed embarrassing bug: the master checksum in the head table is now
   calculated correctly even on little-endian platforms (such as Intel).
-  Made the cmap format 4 compiler smarter: the binary data it creates
   is now more or less as compact as possible. TTX now makes more
   compact data than in any shipping font I've tested it with.
-  Dump glyph names as a separate "GlyphOrder" pseudo table as opposed
   to as part of the glyf table (obviously needed for CFF-OTF's).
-  Added proper support for the CFF table.
-  Don't barf on empty tables (questionable, but "there are font out
   there...")
-  When writing TT glyf data, align glyphs on 4-byte boundaries. This
   seems to be the current recommendation by MS. Also: don't barf on
   fonts which are already 4-byte aligned.
-  Windows installer contributed bu Adam Twardoch! Yay!
-  Changed the command line interface again, now by creating one new
   tool replacing the old ones: ttx It dumps and compiles, depending on
   input file types. The options have changed somewhat.
-  The -d option is back (output dir)
-  ttcompile's -i options is now called -m (as in "merge"), to avoid
   clash with dump's -i.
-  The -s option ("split tables") no longer creates a directory, but
   instead outputs a small .ttx file containing references to the
   individual table files. This is not a true link, it's a simple file
   name, and the referenced file should be in the same directory so
   ttcompile can find them.
-  compile no longer accepts a directory as input argument. Instead it
   can parse the new "mini-ttx" format as output by "ttx -s".
-  all arguments are input files
-  Renamed the command line programs and moved them to the Tools
   subdirectory. They are now installed by the setup.py install script.
-  Added OpenType support. BASE, GDEF, GPOS, GSUB and JSTF are (almost)
   fully supported. The XML output is not yet final, as I'm still
   considering to output certain subtables in a more human-friendly
   manner.
-  Fixed 'kern' table to correctly accept subtables it doesn't know
   about, as well as interpreting Apple's definition of the 'kern' table
   headers correctly.
-  Fixed bug where glyphnames were not calculated from 'cmap' if it was
   (one of the) first tables to be decompiled. More specifically: it
   cmap was the first to ask for a glyphID -> glyphName mapping.
-  Switched XML parsers: use expat instead of xmlproc. Should be faster.
-  Removed my UnicodeString object: I now require Python 2.0 or up,
   which has unicode support built in.
-  Removed assert in glyf table: redundant data at the end of the table
   is now ignored instead of raising an error. Should become a warning.
-  Fixed bug in hmtx/vmtx code that only occured if all advances were
   equal.
-  Fixed subtle bug in TT instruction disassembler.
-  Couple of fixes to the 'post' table.
-  Updated OS/2 table to latest spec.

1.0b1 (released 2001-08-10)
---------------------------

-  Reorganized the command line interface for ttDump.py and
   ttCompile.py, they now behave more like "normal" command line tool,
   in that they accept multiple input files for batch processing.
-  ttDump.py and ttCompile.py don't silently override files anymore, but
   ask before doing so. Can be overridden by -f.
-  Added -d option to both ttDump.py and ttCompile.py.
-  Installation is now done with distutils. (Needs work for environments
   without compilers.)
-  Updated installation instructions.
-  Added some workarounds so as to handle certain buggy fonts more
   gracefully.
-  Updated Unicode table to Unicode 3.0 (Thanks Antoine!)
-  Included a Python script by Adam Twardoch that adds some useful stuff
   to the Windows registry.
-  Moved the project to SourceForge.

1.0a6 (released 2000-03-15)
---------------------------

-  Big reorganization: made ttLib a subpackage of the new fontTools
   package, changed several module names. Called the entire suite
   "FontTools"
-  Added several submodules to fontTools, some new, some older.
-  Added experimental CFF/GPOS/GSUB support to ttLib, read-only (but XML
   dumping of GPOS/GSUB is for now disabled)
-  Fixed hdmx endian bug
-  Added -b option to ttCompile.py, it disables recalculation of
   bounding boxes, as requested by Werner Lemberg.
-  Renamed tt2xml.pt to ttDump.py and xml2tt.py to ttCompile.py
-  Use ".ttx" as file extension instead of ".xml".
-  TTX is now the name of the XML-based *format* for TT fonts, and not
   just an application.

1.0a5
-----

Never released

-  More tables supported: hdmx, vhea, vmtx

1.0a3 & 1.0a4
-------------

Never released

-  fixed most portability issues
-  retracted the "Euro_or_currency" change from 1.0a2: it was
   nonsense!

1.0a2 (released 1999-05-02)
---------------------------

-  binary release for MacOS
-  genenates full FOND resources: including width table, PS font name
   info and kern table if applicable.
-  added cmap format 4 support. Extra: dumps Unicode char names as XML
   comments!
-  added cmap format 6 support
-  now accepts true type files starting with "true" (instead of just
   0x00010000 and "OTTO")
-  'glyf' table support is now complete: I added support for composite
   scale, xy-scale and two-by-two for the 'glyf' table. For now,
   component offset scale behaviour defaults to Apple-style. This only
   affects the (re)calculation of the glyph bounding box.
-  changed "Euro" to "Euro_or_currency" in the Standard Apple Glyph
   order list, since we cannot tell from the 'post' table which is
   meant. I should probably doublecheck with a Unicode encoding if
   available. (This does not affect the output!)

Fixed bugs: - 'hhea' table is now recalculated correctly - fixed wrong
assumption about sfnt resource names

1.0a1 (released 1999-04-27)
---------------------------

-  initial binary release for MacOS
