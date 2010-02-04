# $Id: e-smith-portforwarding.spec,v 1.11 2010/02/04 17:07:02 filippocarletti Exp $

Summary: portforwarding panel for SME Server
%define name e-smith-portforwarding
Name: %{name}
%define version 2.0.0
%define release 2
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-portforwarding-2.2.0-AllowHosts.patch
Patch2: e-smith-portforwarding-2.2.0-AllowHosts.patch2
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
Requires: e-smith-packetfilter >= 1.13.0-13
Requires: e-smith-lib >= 1.15.1-19
Requires: e-smith-formmagick >= 1.4.0-12
BuildRequires: e-smith-devtools >= 1.13.1-03
Obsoletes: e-smith-ipportfw dmc-mitel-portforwarding
AutoReqProv: no

%description
Adds a Port Forwarding panel to the SME server-manager.

%changelog
* Thu Feb 4 2010 Filippo Carletti <filippo.carletti@gmail.com> 2.0.0-2.sme
- Enable port forwards to localhost if mode is serveronly [SME: 1003]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.0.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Sun Apr 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-9
- Add common <base> tags to e-smith-formmagick's general [SME: 4282]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.2.0-8
- Remove <base> tags now in general [SME: 3913]

* Sun Feb 10 2008 Stephen Noble <support@dungog.net> 1.2.0-7
- Remove duplicate <base> entries [SME: 3888]

* Thu Nov 08 2007 Gavin Weight<gweight@mail.com> 1.2.0-6
- Remove/Fix portforwarding.pm.orig file. [SME: 3526]

* Tue Oct 16 2007 Charlie Brady <charlie_brady@mitel.com> 1.2.0-5
- Use $OUTERNET for target of localhost port forwards, not externalIP
  pulled from db at template expansion time. [SME: 2760]

* Wed Jun 26 2007 Shad L. Lords <slords@mail.com> 1.2.0-4
- Ensure portforwarding dbs exists [SME: 54]

* Tue Jun 26 2007 Shad L. Lords <slords@mail.com> 1.2.0-3
- Migrate portforwarding to own databases [SME: 54]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-02
- Bump release number only

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.1.2-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-13]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-12]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Thu Jul 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-11]
- Fix an expression precedence problem with UDP portforwarding. [SF: 1237913]

* Fri Jul  8 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-10]
- Fix UDP portforwarding. [SF: 1234630]

* Sat Mar 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-09]
- Fix typo in createlinks.

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-08]
- Add fr and es localisations for new text.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-07]
- Display text to indicate that portforwarding isn't available in
  serveronly mode.
- Create new portforwarding-update event, as remoteaccess-update
  is rather heavyweight. use generic_template_expand and
  adjust-services.  [MN00064130, MN00065576]
- Fix some run-time probs with Gordon's contributed patch.

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-06]
- Patch provided by Gordon to allow portforwarding to "localhost".

* Wed May  5 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-05]
- Now detecting serveronly mode, and disabling the ability to add
  portforwarding rules while in that state. [msoulier MN00025609]

* Wed Dec  3 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-04]
- Added French and Spanish translations of new lexicon. [msoulier 10203]

* Wed Dec  3 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-03]
- Refactored 91adjustPortForward to remove duplicate code. [msoulier 10203]
- Added code to properly handle portforwarding to the external interface.
  Forwarding to localhost or the private interface is now explicitly blocked.
  [msoulier 10203]

* Mon Oct 20 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-02]
- Added better validation on the sort port to prevent conflicting rules.
  [msoulier 9262]

* Fri Oct 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-01]
- forcing to dev stream - 1.1.0

* Fri Oct 17 2003 Michael Soulier <msoulier@e-smith.com>
- [0.2.0-03]
- Fixed summaries so that the styling is now 6.0. [msoulier 9306]

* Thu Aug 28 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-02]
- Fix typo in masq fragment which prevented forwarding of UDP.
  [charlieb 9859]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-01]
- Changing version to stable stream number - 0.2.0

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.1-20]
- Wording update on main page [gordonr 9101]

* Fri Jun 20 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-19]
- Revert to previous version. [msoulier 8803]

* Wed Jun 11 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.1-18]
- Redo (simplify) some of the code in the portforwarding panel, and make
  destination port explicit if not specified. [charlieb 8803]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.1-17]
- Add Spanish lexicon for portfowarding [lijied 3793]

* Tue Apr  8 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.1-16]
- Removed colons on the label where necessary [lijied 7950]

* Tue Apr  8 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.1-15]
- Modified button Apply to Add [lijied 7921]

* Tue Apr  8 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.1-14]
- Added French translation for "Misuse of feature...." [lijied 8072]

* Tue Apr  8 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-13]
- Fixed lack of buttons on summary page. [msoulier 8089]

* Mon Apr  7 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-12]
- Inserting PortForwarding chain as first entry in the PREROUTING chain.
  [msoulier 8089]

* Fri Apr  4 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.1-11]
- Change $q->table to $q->start_table where necessary [lijied 8034]

* Fri Apr  4 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.1-10]
- Text revision on panel [gordonr 8072]

* Thu Apr  3 2003 Tony Clayton <apc@e-smith.com>
- [0.1.1-09]
- Add colons to labels and fix text when table is empty in panel [tonyc 7950]

* Wed Apr  2 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-08]
- Added french lexicon for creating a port-forwarding rule. [msoulier 7284]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.1-07]
- Delete stray fr nav bar lexicon entries [gordonr 7926]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.1-06]
- Added french lexicon for security, so it shows up in the right spot
  on the menu panel. [msoulier 7284]

* Tue Apr  1 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-05]
- Added proper styling to the tables. [msoulier 7284]
- Added spacing around table elements. [msoulier 7284]
- Put a 6.0 look on the buttons on the summary page. [msoulier 7284]
- Removed the button-like style from the remove links. [msoulier 7284]

* Fri Mar 28 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-04]
- Added proper styles to make links that behave like buttons,
  look like buttons, for 6.0. [msoulier 7284]

* Fri Mar 28 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-03]
- Fixed a couple of typos in the english lexicon. [msoulier 7284]
- Included the french lexicon. [msoulier 7284]

* Tue Mar 25 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-02]
- Portforwarding still had problems, fixed here. [msoulier 7284]

* Tue Mar 25 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.1-01]
- Modified to work with new e-smith-packetfilter changes for 6.0 
  [msoulier 7284]
- Note: This breaks backwards-compatibility with 5.6.

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.0-33]
- Modified port forwarding panel order [lijied 7356]

* Thu Mar 13 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.0-32]
- Split en-us lexicon from portwarding panel [lijied 4030]

* Tue Mar 11 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-31]
- Finished patching the interface to take an empty dport. [msoulier 5645]

* Mon Mar 10 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-30]
- Patched the masq fragments to accept an empty dport. [msoulier 5645]
- Patched the interface to accept an empty destination port. 
  [msoulier 5645]

* Mon Mar 10 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-29]
- Tweaked the wording in the panel. [msoulier 5645]

* Mon Mar 10 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-28]
- Additional tweaks to fix the iptables syntax and adjust the size of the
  fields in the UI. [msoulier 5645]

* Mon Mar 10 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-27]
- Adding support for a port range on source and destination ports.
  [msoulier 5645]

* Mon Mar 10 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-26]
- Updating dependencies. [msoulier 5645]

* Mon Mar 10 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-25]
- Fixed bad removal which set all destination ports to the same port.
  [msoulier 5645]

* Mon Mar 10 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-24]
- Updated dependency information to make it use the backported
  e-smith-packetfilter rpm for the 5.6 updates stream. [msoulier 5645]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.0-23]
- Modified panel order [lijied 7356]

* Sun Feb 23 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-22]
- Backed-out the changes in 0.1.0-21. They're incompatible with
  e-smith-packetfilter. We'll have to discuss this first. [msoulier 5696]

* Sun Feb 23 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-21]
- Permitting port ranges instead of just single ports. [msoulier 5696]

* Sun Jan 26 2003 Mike Dickson <miked@e-smith.com>
- [0.1.0-20]
- added ACTION to lexicon, and code to use it [miked 6363]

* Sun Jan 26 2003 Mike Dickson <miked@e-smith.com>
- [0.1.0-19]
- backed out previous patch since it applied too many changes at once.  I will
  re-submit in manageable chunks

* Sat Jan 25 2003 Mike Dickson <miked@e-smith.com>
- [0.1.0-18]
- added ACTION to lexicon [miked 6363]

* Wed Dec 18 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-17]
- Added a feature to remove the "finished" page and cycle back to the start
  page with a status message instead. [msoulier 5696]
- Found and fixed a bug permitting the addition of duplicate rules.

* Mon Dec 16 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-16]
- Added a space between the two buttons on the summary panel.
  [msoulier 5696]

* Mon Dec 16 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-15]
- Fixed broken removal due to using the wrong variable set to repopulate the
  db entry. [msoulier 5696]

* Fri Dec  6 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-14]
- Fixed bad variable reference in test cases. [msoulier 5696]

* Thu Dec  5 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-13]
- Added some test cases to portforwarding.pm. [msoulier 5696]

* Fri Nov 29 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-12]
- Improved the IP address validation. [msoulier 5696]

* Fri Nov 29 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-11]
- Made sure all messages are localised, and added better error handling.
  [msoulier 5696]

* Thu Nov 28 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-10]
- Updated to make use of changes to the packetfilter. Fixed the placement of
  the udp portforwarding rules, and the spelling of "completely".
  [msoulier 5696]

* Wed Nov 27 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-09]
- Localised the summary table labels. [msoulier 5696]

* Wed Nov 27 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-08]
- The destination host must be an IP address. Enforcing now.
  [msoulier 5696]

* Tue Nov 26 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-07]
- First working prototype. [msoulier 5696]

* Mon Nov 25 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-06]
- Basic functionality present. Still need to add the ability to
  delete rules, and display current rules. [msoulier 5696]

* Fri Nov 22 2002 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-05]
- Starting the FormMagick conversion of the panel. [msoulier 5696]

* Thu Nov 21 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.0-04]
- Use "--list --numeric" to avoid DNS lookup delays. [charlieb 5645]

* Mon Nov 11 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.0-03]
- Fix portforwarding rules to match DB format used by panel code -
  which is $ip:[$dport], this allows forwarding to a port other than the
  listen port [charlieb 5645].

* Mon Nov 11 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.0-02]
- Convert to iptables, and conform to "masq adjust" way of doing things.
  [charlieb 5645]

* Mon Nov 11 2002 Charlie Brady <charlieb@e-smith.com>
- [0.1.0-01]
- Rolling to development stream to 0.1.0

* Mon Nov 11 2002 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-6]
- Renamed to e-smith-portforwarding.
- Imported into CVS as baseline for further development.

* Sat Sep 21 2002 Darrell May <dmay@netsourced.com>
- updated 35SetPortFW to support dynamic external IP
- [0.0.1-5]
* Tue Jan 01 2002 Darrell May <dmay@netsourced.com>
- added Obsoletes: e-smith-ipportfw dmc-mitel-portfowarding
- [0.0.1-4]
* Tue Jan 01 2002 Darrell May <dmay@netsourced.com>
- fixed spelling in rpm name, now to dmc-mitel-portforwarding
- merged in e-smith-ipportfw-0.1.1-1.noarch.rpm
- [0.0.1-3]
* Mon Dec 31 2001 Darrell May <dmay@netsourced.com>
- added "Shad L. Lords" <lists@lordsfam.net>, e-smith-iportfw 35SetPortFW
- templates-custom fragment supporting dest port addresses
- updated portforwarding panel to match
- removed first/last portforward panel bug by adding return on Operation Status
- [0.0.1-2]
* Sun Dec 30 2001 Darrell May <dmay@netsourced.com>
- initial release
- [0.0.1-1]

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f e-smith-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist

for proto in tcp udp
do
    mkdir -p $RPM_BUILD_ROOT/home/e-smith/db
    touch $RPM_BUILD_ROOT/home/e-smith/db/portforward_$proto
    echo "%config(noreplace) %attr(0640,root,admin) /home/e-smith/db/portforward_$proto" \
        >> %{name}-%{version}-filelist
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist

%defattr(-,root,root)

%pre

%post

%preun

%postun
